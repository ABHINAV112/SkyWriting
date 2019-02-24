show = document.getElementById("show")
console.log(show)
displayText=document.getElementById("displayText")
console.log(displayText)

show.addEventListener("click",function(){
    displayText.value = a
})

clear = document.getElementById("clear")
console.log(clear)
clear.addEventListener("click",function(){
    displayText.value=''
})

save = document.getElementById("save")
//Saving text data onto firebase
save.addEventListener("click", function(){
    var db = firebase.firestore()
    console.log(displayText.value)
    if (displayText.value){
          var newDate = new Date();
          var sysTime = newDate.getTime()
          var docName = sysTime.toString()
          var setDoc = db.collection('class').doc(docName).set({text: displayText.value});
    }
})