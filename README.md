# NOTE: THIS IS A SAMPLE README.md, Final version will have updated content
# Document Portal

🚀 **Document Portal** - A comprehensive document processing and retrieval system powered by AI and cloud technologies.

## Overview

Document Portal is an advanced document processing platform that leverages embedding models, synthetic search, and multi-document AI capabilities to provide intelligent document analysis and retrieval services. The system is designed for deployment on AWS with cloud-based embedding storage and offers both programmatic APIs and an intuitive Streamlit UI.

## 🎯 Use Cases

The Document Portal supports four primary use cases:

### 1. Document RAG (Retrieval-Augmented Generation)
- **Purpose**: Enhanced document understanding using embedding models
- **Technology**: Vector embeddings for semantic search and content retrieval
- **Benefits**: Accurate information extraction and context-aware responses

### 2. Document Comparison
- **Purpose**: Intelligent document comparison using synthetic search
- **Technology**: Advanced similarity algorithms and content analysis
- **Benefits**: Identify differences, similarities, and relationships between documents

### 3. Multi-Document Chat
- **Purpose**: Conversational AI across multiple documents simultaneously
- **Technology**: Cross-document context understanding and synthesis
- **Benefits**: Comprehensive insights from document collections

### 4. Single Document Chat
- **Purpose**: Interactive Q&A with individual documents
- **Technology**: Document-specific context understanding
- **Benefits**: Deep dive analysis and targeted information retrieval

## 🏗️ Architecture

### Cloud Infrastructure (AWS)
- **Compute**: AWS Lambda / ECS for API services
- **Storage**: S3 for document storage
- **Database**: Vector database for embeddings (Amazon OpenSearch/Pinecone)
- **AI Services**: Integration with AWS Bedrock or external LLM APIs

### Core Components
- **Embedding Engine**: Document vectorization and storage
- **Search Engine**: Semantic and synthetic search capabilities
- **Chat Engine**: Conversational AI interface
- **Comparison Engine**: Document similarity analysis

## 🔌 API Endpoints

The Document Portal exposes 4 REST APIs to evaluate and interact with the use cases:

```bash
# 1. Document RAG API
POST /api/v1/rag/query
# Query documents using RAG with embedding search

# 2. Document Compare API
POST /api/v1/compare/documents
# Compare multiple documents using synthetic search

# 3. Multi-Document Chat API
POST /api/v1/chat/multi
# Interactive chat across multiple documents

# 4. Single Document Chat API
POST /api/v1/chat/single
# Interactive chat with a single document
```

## 🖥️ User Interface

### Streamlit Application
A comprehensive web application built with Streamlit that provides:
- Document upload and management
- Interactive testing of all 4 use cases
- Real-time API testing interface
- Results visualization and export
- Performance metrics and analytics

**Access**: `streamlit run app.py`

## 🧪 Development & Testing

### Jupyter Notebook Integration
Dedicated Jupyter notebooks for comprehensive testing:
- **`integration_tests.ipynb`**: End-to-end integration tests
- **`api_tests.ipynb`**: API functionality validation
- **`embedding_tests.ipynb`**: Embedding model performance tests
- **`ui_tests.ipynb`**: Streamlit UI component testing

### Testing Workflow
1. **Prototype in Jupyter**: Test all code integration before module implementation
2. **Module Development**: Convert validated code into Python modules
3. **Integration Testing**: Comprehensive testing across all components
4. **API Testing**: Validate all endpoint functionalities
5. **UI Testing**: Ensure Streamlit interface works seamlessly

## 🚀 Getting Started

### Prerequisites
```bash
# Python 3.8+
python --version

# AWS CLI configured
aws configure

# Required packages
pip install -r requirements.txt
```

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/document_portal.git
   cd document_portal
   ```

2. **Set up virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your AWS and API configurations
   ```

### Quick Start

1. **Start the API server:**
   ```bash
   python -m uvicorn main:app --reload
   ```

2. **Launch Streamlit UI:**
   ```bash
   streamlit run streamlit_app.py
   ```

3. **Open Jupyter for testing:**
   ```bash
   jupyter notebook notebooks/
   ```

## 📁 Project Structure

```
document_portal/
├── src/
│   ├── api/                 # API endpoints and routing
│   ├── core/                # Core business logic
│   ├── models/              # Data models and schemas
│   ├── services/            # External service integrations
│   └── utils/               # Utility functions
├── notebooks/               # Jupyter notebooks for testing
│   ├── integration_tests.ipynb
│   ├── api_tests.ipynb
│   ├── embedding_tests.ipynb
│   └── ui_tests.ipynb
├── streamlit_app.py         # Streamlit UI application
├── main.py                  # FastAPI application entry point
├── requirements.txt         # Python dependencies
├── docker-compose.yml       # Local development setup
├── aws/                     # AWS deployment configurations
└── tests/                   # Unit and integration tests
```

## 🔧 Configuration

### Environment Variables
```bash
# AWS Configuration
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_REGION=us-east-1

# Database Configuration
VECTOR_DB_URL=your_vector_db_url
VECTOR_DB_API_KEY=your_api_key

# AI Model Configuration
OPENAI_API_KEY=your_openai_key
EMBEDDING_MODEL=text-embedding-ada-002
LLM_MODEL=gpt-4
```

## 🧪 Testing

### Run All Tests
```bash
# Unit tests
python -m pytest tests/unit/

# Integration tests
python -m pytest tests/integration/

# API tests
python -m pytest tests/api/
```

### Jupyter Notebook Testing
```bash
# Start Jupyter and run test notebooks
jupyter notebook notebooks/integration_tests.ipynb
```

## 🚀 Deployment

### AWS Deployment
```bash
# Deploy using AWS CDK or CloudFormation
aws cloudformation deploy --template-file aws/cloudformation.yml

# Or using Docker
docker build -t document-portal .
docker run -p 8000:8000 document-portal
```

## 📊 Performance Metrics

- **Response Time**: < 2s for document queries
- **Throughput**: 100+ concurrent requests
- **Accuracy**: 95%+ for document retrieval
- **Scalability**: Auto-scaling based on demand

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Test your changes in Jupyter notebooks first
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

### Development Workflow
1. **Prototype** → Jupyter Notebooks
2. **Develop** → Python Modules
3. **Test** → Integration Tests
4. **Deploy** → AWS Infrastructure

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

For support and questions:
- Create an issue in the GitHub repository
- Check the documentation in the `docs/` folder
- Review the Jupyter notebooks for implementation examples

---

**Built with ❤️ for intelligent document processing**
