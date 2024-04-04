from textExtraction import extract_text_from_pdf
pdf_text = extract_text_from_pdf('C:/Users/Mustafa Syed/Desktop/resumeschezeenfazulbhoy.pdf')
print(pdf_text)

# Replace 'your_pdf_file.pdf' with the path to your PDF file
Json_form='''{
    "name": "XYZ",
    "contact": {
        "email": "xyz@gmail.com",
        "phone": "+1-123-456-7890",
        "website": "http://www.xyz.com"
    },
    "education": [
        {
            "institution": "Georgia Institute of Technology",
            "location": "Atlanta, GA",
            "degree": "Master of Science in Computer Science",
            "gpa": "4.00",
            "dates": "Aug. 2012 -- Dec. 2013"
        },
        {
            "institution": "Birla Institute of Technology and Science",
            "location": "Pilani, India",
            "degree": "Bachelor of Engineering in Electrical and Electronics",
            "gpa": "3.66 (9.15/10.0)",
            "dates": "Aug. 2008 -- July. 2012"
        }
    ],
    "experience": [
        {
            "company": "Google",
            "location": "Mountain View, CA",
            "position": "Software Engineer",
            "dates": "Oct 2016 - Present",
            "responsibilities": [
                "TensorFlow: TensorFlow is an open source software library for numerical computation using data flow graphs; primarily used for training deep learning models. Worked on APIs and performance for training models on Tensor Processing Units (TPU).",
                "Apache Beam: Apache Beam is a unified model for defining both batch and streaming data-parallel processing pipelines, as well as a set of language-specific SDKs for constructing pipelines and runners."
            ]
        },
        {
            "company": "Coursera",
            "location": "Mountain View, CA",
            "position": "Senior Software Engineer",
            "dates": "Jan 2014 - Oct 2016",
            "responsibilities": [
                "Notifications: Service for sending email, push and in-app notifications. Involved in features such as delivery time optimization, tracking, queuing and A/B testing. Built an internal app to run batch campaigns for marketing etc.",
                "Nostos: Bulk data processing and injection service from Hadoop to Cassandra and provides a thin REST layer on top for serving offline computed data online.",
                "Workflows: Dataduct an open source workflow framework to create and manage data pipelines leveraging reusables patterns to expedite developer productivity.",
                "Data Collection: Designed the internal survey and crowd sourcing platform which allowed for creating various tasks for crowd sourcing or embedding surveys across the Coursera platform.",
                "Dev Environment: Analytics environment based on docker and AWS, standardized the python and R dependencies. Wrote the core libraries that are shared by all data scientists.",
                "Data Warehousing: Setup, schema design and management of Amazon Redshift. Built an internal app for access to the data using a web interface. Dataduct integration for daily ETL injection into Redshift.",
                "Recommendations: Core service for all recommendation systems at Coursera, currently used on the homepage and throughout the content discovery process. Worked on both offline training and online serving.",
                "Content Discovery: Improved content discovery by building a new onboarding experience on coursera. Using this to personalize the search and browse experience. Also worked on ranking and indexing improvements.",
                "Course Dashboards: Instructor dashboards and learner surveying tools, which helped instructors run their class better by providing data on Assignments and Learner Activity."
            ]
        },
        {
            "company": "Lucena Research",
            "location": "Atlanta, GA",
            "position": "Data Scientist",
            "dates": "Summer 2012 and 2013",
            "responsibilities": [
                "Portfolio Management: Also creating a strategy backtesting engine used for simulating and backtesting strategies.",
                "QuantDesk: Python backend for a web application used by hedge fund managers for portfolio management."
            ]
        },
        {
            "company": "Georgia Institute of Technology",
            "location": "Atlanta, GA",
            "position": "Research and Teaching Assistant",
            "dates": "Jan 2012 - Dec 2013",
            "responsibilities": [
                "Research Assistant - Machine Learning: Research on machine learning for portfolio hedging and replication algorithms. Modeling low-risk \\& continuous-return strategies. Developed the python library QSTK.",
                "Teaching Assistant - Computational Investing: The online course on Coursera, had more than 100,000 students enrolled. It was featured on the 11 Alive News and the Atlanta Journal Constitution. Involved in creating assignment, exams and conducting recitation sessions. Also taught the on-campus version of the course."
            ]
        }
    ],
    "skills": [
        {
            "skillName": "Programming Languages",

            "list": "C, C++, Java, Python"
        },
        {
            "skillName": "Web Technologies",

            "list": "HTML5, CSS3, JavaScript, React.js, React Native, Node.js, Express.js, TypeScript, web sockets"
        },

        {
            "skillName": "Developer Tools",

            "list": "Linux, Shell, Git/GitHub, RESTful API\u2019s"
        },
        {
            "skillName": "Soft Skills",

            "list": "Leadership, Team Player, Problem Solving, Project Management, Design Thinking, Decision Making"
        },
        {
            "skillName": "Databases \\& Cloud",

            "list": "MySQL, MongoDB, PostgreSQL, Oracle SQL, AWS (EC2, S3, DynamoDB), Docker"
        }
    ],
    "projects": [
        {
            "name": "QuantSoftware Toolkit",
            "description": [
              "Open source Python library for financial data analysis and machine learning for finance.",
              "Developed via python"
               ]
        },
        {
            "name": "Github Visualization",
             "description": [
             "Data Visualization of Git Log data using D3 to analyze project trends over time."
             ]
        }
    ]
}

'''
#chatgpt code sample to generate resumes
import requests
import json
#api_key=""
headers = {
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {api_key}',
                }

# The data to be sent in the POST request
data = {
    "model": "gpt-3.5-turbo-0125",
    "response_format": {"type": "json_object"},
    "seed":1,
    "messages": [
    {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
   # {"role": "user", "content": f'''{pdf_text} ,{Json_form} < This is my existing resume pdf_text. Now take the content from pdf_text and edit the json_form such that it fit exactly fit to the same structure(object key) of json_form. In project desription- mention the full description. Dont add Additional new objects in json form and dont change the object key. Strictly Keep the object key same. If any from pdf_text you are not able to get some object key value, keep the key name and value it with empty string.  >'''}#prompt
    {"role": "user", "content": f'''{pdf_text} ,{Json_form} <  This is my existing resume pdf_text. I want to update the JSON structure (object keys) to match the existing JSON form. Do not add any new objects to the JSON form and do not change the object keys. Keep the object keys exactly the same. If any values are missing from the resume text, fill them with empty strings. Dont copy content(object values) from the json_form object values exact,if any object value isnt mentioned in pdftext then dont include it(example: if the json_form have any education and pdf_text doesnt dont include it. since we are just taking the format of json form and not the content).strictly the object value should be based on unique pdf_text. If any objects are not present in pdf_text such as projects or skills etc, do not consider it then, ONly consider what is in the pdf_text>'''}#prompt

    ]
}

# Making the POST request
openai_endpoint = 'https://api.openai.com/v1/chat/completions'
response = requests.post(openai_endpoint, headers=headers, data=json.dumps(data))

# Checking if the request was successful
if response.status_code == 200:
    # Assuming the response content follows the format you're expecting
    response_content = response.json()
    # This would be your line to extract the specific message content and load it as JSON, adjusted for actual API response structure
    extracted_response = response_content.get('choices', [{}])[0].get('message', {}).get('content', {})
    response=json.loads(extracted_response)
    print (response)

def remove_unicode_and_replace_special_characters(data):
    replacements = {
        '#': r'\#',
        '$': r'\$',
        '%': r'\%',
        '^': r'\^{}',
        '&': r'\&',
        '_': r'\_'
    }

    if isinstance(data, dict):
        return {key: remove_unicode_and_replace_special_characters(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [remove_unicode_and_replace_special_characters(item) for item in data]
    elif isinstance(data, str):
        # Remove Unicode characters
        data = data.encode('ascii', 'ignore').decode('ascii')
        # Replace special characters
        for old, new in replacements.items():
            data = data.replace(old, new)
        return data
    else:
        return data

# Apply both operations to the response
cleaned_response = remove_unicode_and_replace_special_characters(response)

print(cleaned_response)
with open('data1.json', 'w') as json_file:
    json.dump(cleaned_response, json_file, indent=4)