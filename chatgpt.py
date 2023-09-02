import openai




                       


openai.api_key = "paste your key"



while True:
        user= input("enter your question:  ")
        model="text-davinci-003"
        
    
        completion= openai.Completion.create(model="text-davinci-003",
        prompt= user,
        max_tokens= 1007,
        temperature= 0.5,
        top_p= 1,
        n= 1,
        stop=None)


        response= completion.choices[0].text
        
        print(response)
        

    
