# Backend for an ecommerce application

This is an attempt to create a backend for an ecommerce website. 
## Functionality:
  1. Register & login with mobile number and OTP as a seller or a buyer. 
    - Created Serializer and views for Login Request, OTP Request, OTP Response, SignUp. 
    - This allows us to create users and bypass the OTP verification to signup and login.
    - Token is given to users upon verification. This lacks the functionality to delete tokens after a given time. 
  2. Sellers can create their store with phone number and store name. 
  3. Sellers can have multiple stores and ability to upload products. 
  4. Sellers get a store link which can produce basic store details or give a product catelog depending on the API call.
  5. Buyers can add products to their carts. 
  6. Buyers can convert cart items into an order. 

## Functionality still being worked on:
 
  1. Make sure that photos can be uploaded with products. Need to add an Image field. 
