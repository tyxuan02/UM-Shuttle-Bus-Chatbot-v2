## UM Shuttle Bus Chatbot v2.0

UM Shuttle Bus Chatbot is chatbot designed to provide information about UM shuttle bus schedules, routes and FAQs. BWith the power of JamAI Base, an open-source Backend-as-a-Service (BaaS) for managing workflows of large language models (LLMs), the chatbot can respond to different user queries. The chatbot is implemented using Python and Streamlit.

### Features

The chatbot can provide information on the following topics:

1. Bus Routes
- Get detailed information about routes for each bus.
- Find shuttle bus stops for specific routes (e.g., "Where are the shuttle bus stops for route AB?").
- Discover which buses stop at a specific location (e.g., "Which buses go to Kolej Kediaman Kinabalu bus stop?").

2. Bus Schedules
- View the schedule for a specific bus or route (e.g., "What is the bus schedule for today?").
- Check when the next trip for a particular route is scheduled (e.g., "When is the next trip for route 13?").

3. Bus Frequency
- Learn about how often buses run and their operating intervals.
- Get information on how long buses take to travel between stops.
- Find out the earliest and latest times buses operate each day.

4. General Information and FAQs
- Access the operating hours of the shuttle bus service.
- Understand requirements for using the service (e.g., "Do I need a UM student card?").
- Find contact information for lost-and-found inquiries.
- Learn about guidelines and special arrangements for shuttle bus usage (e.g., "Can I reserve the shuttle bus for a special event?").

### Limitations

The chatbot currently has the following limitation:

1. Route Suggestions
It cannot suggest direct routes between two specific bus stops. Instead, it provides information about available bus routes or stops based on single-input queries (e.g., "Which buses go to the KK1 bus stop?").

2. Real-Time Updates and Delays
It does not provide real-time information on bus locations or delays. The chatbot is designed to offer general information about bus schedules, routes, and FAQs.

### Run it locally

Download required libraries: `pip install -r requirements.txt`

Upgrade streamlit to the latest version: `pip install --upgrade streamlit`

Train the model for the chatbot (Optional, as the model is already trained and saved as `model.h5`): `python train.py`

Run the chatbot: `streamlit run 1_Chatbot.py`

### Run it on Streamlit

Run the chatbot on Streamlit: [UM Shuttle Bus Chatbot](https://um-shuttle-bus-chatbot-ewe5vzhmtefsskb4n7925g.streamlit.app/)
