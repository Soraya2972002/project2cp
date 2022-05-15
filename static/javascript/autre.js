const selector = document.querySelectorAll(".hidden_ele")
const a_hover = document.querySelectorAll(".a_hover")



selector.forEach(function(element){
    element.addEventListener("click",(e)=>{
      const li_hide =  e.currentTarget.parentElement
      const rotate = e.currentTarget.querySelector(".fa-angle-down")
      li_hide.classList.toggle("hide_sub")
      rotate.classList.toggle("fa-rotate-180")
    })
})

a_hover.forEach((element)=>{
  element.addEventListener("mouseover",(e)=>{
      const nav_hover = e.currentTarget.querySelector(".nav_hover")
      nav_hover.style.height = "90%";
  })
  element.addEventListener("mouseout",(e)=>{
      const nav_hover = e.currentTarget.querySelector(".nav_hover")
      const current = e.currentTarget
      if( !current.classList.contains("current_place")){
        nav_hover.style.height = "0%";
      }
  })
})
/*document.getElementById('id_for_wilaya').addEventListener('change', function(){
  document.getElementById('id_for_commune').innerHTML = "";
  $.ajax({
    type : 'POST',
    url : "products/get_commune",
    data : {
      wilaya : $("#d_for_wilaya").val(),
    },
    dataType : 'json',
    success:function(response){
      var select = document.getElementById(id_for_commune);
      for(var i = 0; i < response.communes.length ; i++){
        var option = document.createElement("option");
        option.value = response.courses[i]["Commune_Name"];
        select.appendChild(option)
      }
    }
  }) 
});*/