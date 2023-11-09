from flask import Flask, request

app = Flask(__name__)
    
@app.route('/', methods=['GET'])    
def get_block_list():
        return {"message":'Welcome'}

if __name__=="__main__":    
    app.run(host="0.0.0.0", port=3000)