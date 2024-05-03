# Vendor-Management-System


# Introduction
This API provides functionalities for managing vendors, purchase orders, and tracking vendor performance metrics.

# Setup Instructions
  ### 1.Clone the Repository:
        Clone this repository to your local machine using the following command
        https://github.com/akshayakumar1/Vendor-Management-System.git
        
  ### 2.Create Virtual Envirmoment & Install Dependencies:
        Navigate to the project directory and install the required dependencies using pip
        
         virtualenv env
         
         activate it
         linux   : source env/bin/activate
         Windos  : C:\> <venv>\Scripts\activate.bat

         cd vendor-management-api
         pip install -r requirements.txt
         
  ### 3.Database Setup: 
        Here im using defult sqlite3 DB. If you want to use PostgreSQL then Update the database inside project>settings>settings.py accordingly.
        DATABASES = {
        'default': {
    
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
    
            'NAME': ‘<db_name>’,
    
            'USER': '<db_username>',
    
            'PASSWORD': '<password>',
    
            'HOST': '<db_hostname_or_ip>',
    
            'PORT': '<db_port>',
              }
      }
        
  ### 4.Apply Migrations & Migrate: 
        Apply the migrations to create the necessary database tables
        
        python manage.py makemigrations
        python manage.py migrate
  ### 5.Run the Development Server: 
        Start the development server to run the API locally
        python manage.py runserver
  ### 6.Access the API: 
        You can now access the API at http://127.0.0.1:8000/



# API Endpoints
  ### Vendor Management:
        POST /api/vendors/: Create a new vendor.
        GET /api/vendors/: List all vendors.
        GET /api/vendors/{vendor_id}/: Retrieve details of a specific vendor.
        PUT /api/vendors/{vendor_id}/: Update details of a specific vendor.
        DELETE /api/vendors/{vendor_id}/: Delete a specific vendor.
        
 ###  Purchase Order Tracking:
        POST /api/purchase_orders/: Create a new purchase order.
        GET /api/purchase_orders/: List all purchase orders.
        GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.
        PUT /api/purchase_orders/{po_id}/: Update details of a specific purchase order.
        DELETE /api/purchase_orders/{po_id}/: Delete a specific purchase order.
        
 ###  Performance Metrics:
        GET /api/vendors/{vendor_id}/performance/: Retrieve performance metrics for a specific vendor.
        
 ###  Acknowledgment Endpoint:
        POST /api/purchase_orders/{po_id}/acknowledge/: Acknowledge a purchase order.
        
 ###  Authentication
        Token-based authentication is used to secure the API endpoints.
        To authenticate requests, include a token in the Authorization header with the prefix Token
        
        headersList = {
         "Accept": "*/*",
         "User-Agent": "Thunder Client (https://www.thunderclient.com)",
         "Authorization": "Token <your_user_token>" 
          }
          
          if your facing any issu for 
          then create token from backend side.
          
            python manage.py shell
            Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] on linux
            Type "help", "copyright", "credits" or "license" for more information.
            (InteractiveConsole)
            
            >>> from django.contrib.auth.models import User
            >>> from rest_framework.authtoken.models import Token
            >>> user = User.objects.get(username='test')
            >>> print(user)
            test
            >>> token, created = Token.objects.get_or_create(user=user)
            >>> print(token)
            085677aafe089380dc0464e5616ff69379be91ff
            >>> print(cre
            created    credits()  
            >>> print(created)
        






  

