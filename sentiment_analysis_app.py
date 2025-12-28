import streamlit as st
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import plotly.express as px
st.set_page_config(page_title="Sentiment Analysis System",page_icon="https://static.vecteezy.com/system/resources/previews/026/226/868/non_2x/sentiment-analysis-icon-illustration-vector.jpg")
st.title("Sentiment Analysis System")
choice=st.sidebar.selectbox("My Menu",("Home","Analysis","Results"))
if(choice=="Home"):
    st.image("https://miro.medium.com/v2/1*_JW1JaMpK_fVGld8pd1_JQ.gif")
    st.write("This is a Natural Language Processing Application which can analyze the sentiment on text data.")
    st.write("This application predict the sentiment into 3 categories,Positive, Negative and Neutral.")
    st.write("This application then visualizes the results based on different different factors such as age, gender, language, city.")
elif(choice=="Analysis"):
    sid=st.text_input("Enter your Google Sheet ID")
    r=st.text_input("Enter range between first column and last Column")
    c=st.text_input("Enter column name that is to be analyzed")
    btn=st.button("Analyze")
    if(btn):
        if 'cred' not in st.session_state:
            f=InstalledAppFlow.from_client_secrets_file("key.json",["https://www.googleapis.com/auth/spreadsheets"])
            st.session_state['cred']=f.run_local_server(port=0)
        mymodel=SentimentIntensityAnalyzer()
        service=build("Sheets","v4",credentials=st.session_state['cred']).spreadsheets().values()
        k=service.get(spreadsheetId=sid,range=r).execute()
        d=k['values']
        df=pd.DataFrame(data=d[1:],columns=d[0])
        l=[]
        for i in range(0,len(df)):
            t=df._get_value(i,c)
            pred=mymodel.polarity_scores(t)
            if(pred['compound']>0.5):
                l.append("Positive")
            elif(pred['compound']<-0.5):
                l.append("Negative")
            else:
                l.append("Neutral")
        df['Sentiment']=l
        df.to_csv("results1.csv",index=False)
        st.subheader("The Analysis results are saved by the name of results1.csv file")
elif(choice=="Results"):
    df=pd.read_csv("results1.csv")
    choice2=st.sidebar.selectbox("Choose Visualization",("None","Pie Chart","Scatterplot","Histogram"))
    st.dataframe(df)
    if(choice2=="Pie Chart"):
        posper=(len(df[df['Sentiment']=='Positive'])/len(df))*100
        negper=(len(df[df['Sentiment']=='Negative'])/len(df))*100
        neuper=(len(df[df['Sentiment']=='Neutral'])/len(df))*100
        fig=px.pie(values=[posper,negper,neuper],names=['Positive','Negative','Neutral'])
        st.plotly_chart(fig)
    if(choice2=="Scatterplot"):
        k=st.text_input("Choose the Continous Column")
        if k:
            fig=px.scatter(x=df[k],y=df['Sentiment'])
            st.plotly_chart(fig)
    if(choice2=="Histogram"):
        k=st.selectbox("Choose Column",df.columns)
        if k:
            fig=px.histogram(x=df[k],color=df['Sentiment'])
            st.plotly_chart(fig)
