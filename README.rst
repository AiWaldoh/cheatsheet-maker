==================================
Cheatsheet Maker - README
==================================

Repository Information
----------------------

- **GitHub Repository**: `https://github.com/AiWaldoh/cheatsheet-maker.git`

Installation and Setup
----------------------

1. Ensure you have `poetry` installed. If not, you can get it via:

   .. code-block:: bash

      pip install poetry

2. Clone the repository:

   .. code-block:: bash

      git clone https://github.com/AiWaldoh/cheatsheet-maker.git
      cd cheatsheet-maker

3. Install the dependencies using `poetry`:

   .. code-block:: bash

      poetry install

Running the Application
-----------------------

To run the app, use the following command:

.. code-block:: bash

   poetry run streamlit run cheatsheet_maker/app.py

About the Application
----------------------

The application is designed to take a Linux command as input and format it in a cheatsheet style using the GPT-3.5 model from OpenAI. Once a command is entered, it queries the API and provides a formatted command which can then be copied for reference.

