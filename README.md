### Project Overview: 
To generate a blog for the User topic with Titan Text G1 - Express Model that runs on the Amazon Bedrock. The user topic will be passed as a POST API request (via postman) .

🛠️ Technologies Used:
1. Llama3 Instruct 8B llm, 
2. Ollama 
3. Serper google search engine API
4. Python 3.10.

### Prerequisites
#### Environment Setup

1. **Create a Virtual Environment using pip:**
   ```bash
   python -m venv llama3_agent_env
   ```
   
3. **Activate the Virtual Environment:**
   ```bash
     llama3_agent_env\Scripts\activate.bat
   ```
#### Setup Ollama Server
1. **Download Ollama:**
   Download [https://ollama.com/download](Ollama)

2. **Download an Ollama Model:**
   ```bash
   curl http://localhost:11434/api/pull -d "{\"name\": \"llama3\"}"
   ```
Ollama[https://github.com/ollama/ollama/blob/main/docs/api.md#list-local-models](API documentionation)

### Clone and Navigate to the Repository

1. **Navigate to the Repo:**
   ```
   cd /path/to/your-repo/custom_websearch_llm_agent_with_llama3_instruct_8B_using_ollama
   ```

2. **Install Requirements:**
   ```
   pip3 install -r requirements.txt
   ```

### Configure API Keys

1. **Open the `config.yaml`:**
   ```
    config.yaml
   ```

2. **Enter API Keys:**
   - **Serper API Key:** Get it from [https://serper.dev/](https://serper.dev/)
   
### Agent Schema:

![Agent Schema](assets/agent_schema.png)

### Run Your Query
```
python agent.py run
```
Then enter your query.

Here the query passed 'what is the population of chennai' ?

chennai wikipedia [https://en.wikipedia.org/wiki/Chennai]

#### Planning agent 

Planning agent created 3 different queries for the input passed .

![Planning Agent](assets/planning_agent.png)

#### Integration agent 

Integration agent takes the queries from planning agent and checks whether it has the sufficient information to answer User custom query.

![Integration Agent](assets/integration_agent.png)

#### Final Response  

If there was sufficient information, Integration agent compiles a response from the best sites visited.
Quality assessment will be made on the integration agent response and a final response will be created if the criteria is met.

![Final Response](assets/final_response.png)

Jun 2024 - Jun 2024


### Summary:

1. Pulled llama3 instruct 8B fine-tuned LLM in ollama ( framework to run llm models locally)
2. Used serper as the primary tool for the search engine query intened for google search.
3. Created planning agent to take user custom query as input and generate searchable queries.
4. Created Integration agent to validate planning agent output and make a google search.
5. Integration agent visited the sites and scraped the best pages to compile a response.
6. Made a quality assessment on the compiled response and generated the final response if the response criteria was met.
