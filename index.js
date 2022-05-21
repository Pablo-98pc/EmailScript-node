const {PythonShell} = require('python-shell')
const express = require('express')
const cors = require('cors')
const app = express()
app.use(cors())
app.use(express.json())


app.post('/api/sendmails',(request,response)=>{
const {emails,msg_content,subject} = request.body

const pyshell = new PythonShell('sendmail.py')

const data ={'emails' : emails , 'msg_content' : msg_content , 'subject' : subject}

pyshell.send(JSON.stringify(data),{mode:'json'})

pyshell.on('message',results=> {
    console.log(results);
    
})

pyshell.end(err=> {
    if (err) console.log(err)
  });

response.send('Sent succesfully')
  
})

const PORT = 4000
app.listen(PORT,()=> {
    console.log(PORT)
});