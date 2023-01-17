// some e mostra
var login = document.getElementById('tab-login');
      var register = document.getElementById('tab-register');
      var camplogin = document.getElementById('pills-login');
      var campregister = document.getElementById('pills-register');
      login.onclick = function() {
        campregister.classList.remove("active");
        camplogin.classList.add("active");
        register.classList.remove("active");
        login.classList.add("active");
      };
      register.onclick = function() {
        camplogin.classList.remove("active");
        campregister.classList.add("active");
        login.classList.remove("active");
        register.classList.add("active");
      };

// lembra de mim
var button = document.getElementById('signin');
var input = document.getElementById('loginName');

button.onclick = function() {
  if (document.getElementById('loginCheck').checked == true){
    valor = document.getElementById('loginName').value
    localStorage.setItem('email',valor)
  }
  else{
    localStorage.removeItem('email');
  }
};

if (localStorage.email == undefined){
  document.getElementById('loginName').setAttribute('value','');
} else {
  document.getElementById('loginName').setAttribute('value',localStorage.email);
}