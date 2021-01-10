const getResp = function() {
    var requestData = document.getElementById("textInput").value;
    fetch('https://xxi6q9rpgk.execute-api.us-east-1.amazonaws.com/prod/medlate',{
        method: 'POST',
        body: JSON.stringify
        ({input: requestData}),
        headers: {
            'Content-type': 'application/json; charset=UTF-8'
        }
    }).then(function(response){
        console.log(response)
    })
}