# AI_stock_analysis
An AI‑powered stock analysis tool inspired by AutoGen‑style multi‑agent workflows. It retrieves real‑time market data and generates educational investment insights using a custom multi‑agent reasoning system. Not financial advice.


AI Stock Analysis Platform
Multi‑Agent AI system inspired by AutoGen — for educational investment insights
An AI‑powered stock analysis tool that retrieves real‑time market data and generates educational investment insights using a custom multi‑agent reasoning pipeline (Researcher → Analyst → Summariser).
Built with Streamlit, OpenAI, and an AutoGen‑inspired agent architecture.

Features
Multi‑Agent Reasoning System
A lightweight, custom agent pipeline inspired by AutoGen:
• 	Researcher Agent — gathers factual stock data and recent news
• 	Analyst Agent — interprets trends, risks, and opportunities
• 	Summariser Agent — produces a clear, investor‑friendly report

Real‑Time Market Data
Integrated with  to fetch:
• 	Current stock price
• 	Market cap
• 	Volume
• 	PE ratio
• 	52‑week range
• 	And more
AI‑Generated Insights
The system provides:
• 	Trend interpretation
• 	Risk assessment
• 	Opportunity analysis
• 	Educational investment guidance
Streamlit Web App
• 	Clean, responsive UI
• 	Sidebar configuration
• 	Quick stock metrics
• 	Downloadable analysis reports
• 	Works in any browser

Architecture Overview

This design is inspired by AutoGen’s multi‑agent workflow, but implemented using the modern OpenAI SDK for stability and long‑term compatibility.

Installation
Clone the repository:

Install dependencies:

Create a  file:

Run the app:


Deployment (Streamlit Cloud)
This app can be deployed easily on Streamlit Community Cloud:
1. 	Push your code to GitHub
2. 	Go to https://streamlit.io/cloud
3. 	Click New App
4. 	Select your repo
5. 	Deploy
You can then share your public link with anyone.

Project Structure


API Key Handling
The app supports two modes:
Local development
Uses  file.
Streamlit Cloud
Use:

The app automatically detects and uses the correct key.

Downloadable Reports
Each analysis can be exported as a Markdown report, including:
• 	Timestamp
• 	User query
• 	Full AI‑generated analysis
Perfect for sharing or saving your insights.

Disclaimer
This application is intended solely for educational and research purposes.
It does not provide financial, investment, or trading advice.
Always consult a licensed financial professional before making investment decisions.

Acknowledgements
• 	Inspired by Microsoft’s AutoGen multi‑agent concepts
• 	Built using OpenAI’s modern SDK
• 	UI powered by Streamlit
• 	Market data from yfinance

Future Enhancements
Planned improvements include:
• 	Stock comparison mode
• 	Sentiment analysis from news sources
• 	Technical indicator charts (RSI, MACD, moving averages)
• 	Portfolio simulation tools
• 	PDF report export
