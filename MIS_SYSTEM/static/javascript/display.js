/*var myID;
function openForm(clicked_id){
  
    if (document.getElementById('mahal').value ==  clicked_id ){
        document.querySelector('.bg-modal').style.display = 'flex';
    }
}*/

$('#modal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget), // Button that triggered the modal  char english
        content = button.siblings('.read-more').html(),//huh!? hotdog
        modal = $(this);
  
    modal.find('.modal-body').html(content);
  });

function closeForm(){
    document.querySelector('.bg-modal').style.display = 'none';
}

function myFunction() {
    alert("You have succesfully Approved the request");
}


$(document).ready(function(){
    $("#modal_ID").click(function(){
        var y = document.getElementById("name").value;
        document.querySelector(".bg-modal").style.display='flex';
        var x = $(this).text
        $.ajax({
            type: 'GET',
            data:{'button_text':"jeje"},
            dataType: 'json',
            success:function(response){
                $("#name").value(response.memoID)
                document.querySelector(".bg-modal").style.display='flex';
            }
        })
    }); 
}); 