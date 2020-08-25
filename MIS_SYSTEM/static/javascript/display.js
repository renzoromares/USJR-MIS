var myID;
function openForm(clicked_id){
  
    if (document.getElementById('mahal').value ==  clicked_id ){
    document.querySelector('.bg-modal').style.display = 'flex';
    
    }
    //alert(clicked_id);
    alert(document.getElementById('types').value);
    
    
    
}

function closeForm(){
    document.querySelector('.bg-modal').style.display = 'none';
}

function myFunction() {
    alert("You have succesfully Approved the request");
}
