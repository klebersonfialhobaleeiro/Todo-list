$(window).on("load", function (e) {
  e.preventDefault();

  $.ajax({
    type: 'GET',
    url: '/total-sum',
    datatype: "json",
    success: function (data) {
      document.getElementById('total').innerHTML = ""
      document.getElementById('total').innerHTML = data.total  
    },
    error: (error) => {
      console.log("error");
    }
  }); 

  $.ajax({
    type: 'GET',
    url: '/relatorio',
    datatype: "json",
    success: function (data) {
      var value = data.value
      var labelsrelatorio = data.labels

      graficoline(value, labelsrelatorio)
    
    },
    error: (error) => {
      console.log("error");
    }
  }); 

  $.ajax({
    type: 'GET',
    url: '/status',
    datatype: "json",
    success: function (data) {
      var atividades = data.atividade
      var labelssatatus = data.labels

      graficodoughnut(atividades, labelssatatus)
      
    },
    error: (error) => {
      console.log("error");
    }
  }); 

})

function graficodoughnut(atividades, labelssatatus) {
  var ctx = document.getElementById("myPieChart");
  var myPieChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: labelssatatus,
      datasets: [{
        data: atividades,
        backgroundColor: ['#e34234', '#ffd700', '#a2cd5a'],
        hoverBackgroundColor: ['#e34234', '#ffd700', '#a2cd5a'],
        hoverBorderColor: "rgba(234, 236, 244, 1)",
      }],
    },
  });
}

function graficoline(value, labelsrelatorio) {
  var Line = document.getElementById("myAreaChart");
  var myLineChart = new Chart(Line, {
    type: 'line',
    data: {
      labels: labelsrelatorio,
      datasets: [{
        label: "Quantidade",
        lineTension: 0.3,
        backgroundColor: "rgba(78, 115, 223, 0.05)",
        borderColor: "rgba(78, 115, 223, 1)",
        pointRadius: 3,
        pointBackgroundColor: "rgba(78, 115, 223, 1)",
        pointBorderColor: "rgba(78, 115, 223, 1)",
        pointHoverRadius: 3,
        pointHoverBackgroundColor: "rgba(78, 115, 223, 1)",
        pointHoverBorderColor: "rgba(78, 115, 223, 1)",
        pointHitRadius: 10,
        pointBorderWidth: 2,
        data: value,
      }],
    },
  });
}