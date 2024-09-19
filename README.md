# Customer Support AI for Airline

This project is a customer support AI designed for an airline, enabling users to research and make travel arrangements seamlessly. Built using Langchain, Langgraph, Tavily, and OpenAI, this AI can assist users in finding and booking flights, hotels, car rentals, excursions, and more.

## Features

- **Flight Information**: Get real-time data on flight schedules, prices, and availability.
- **Hotel Reservations**: Search for and book hotels based on user preferences and budgets.
- **Car Rentals**: Find and reserve rental cars for travel convenience.
- **Excursion Booking**: Explore and book local excursions for an enhanced travel experience.
- **Safe Tool Configuration**: Implement "safe tools" for actions like booking a flight, requiring user confirmation before proceeding.

## Prerequisites

- Python 3.x
- Required libraries (will be installed automatically)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/customer-support-ai.git
   cd customer-support-ai
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Setup

1. **Create the SQLite Database**: Before running the main application, you need to create the database. Run the following command:

   ```bash
   python db.py
   ```

2. **Run the Application**: After the database is set up, you can start the application with:

   ```bash
   python main.py
   ```

## Usage

Once the application is running, you can interact with the AI via the command line. 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Langchain](https://langchain.com/)
- [Langgraph](https://github.com/LangGraph/langgraph)
- [Tavily](https://tavily.com/)
- [OpenAI](https://openai.com/)