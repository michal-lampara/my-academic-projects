<!DOCTYPE html>
<html>
<head>
	<title>Koszyk</title>
</head>
<body>
	<h1>Koszyk</h1>
	
</body>
</html>

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Moja strona</title>
  <link href="css/style.css" rel="stylesheet" type="text/css" />
  <link href="css/button.css" rel="stylesheet" type="text/css">
  <link href="css/clock.css" rel="stylesheet" type="text/css">
      <link href="css/fontello.css" type="text/css" rel="stylesheet">
  <style>
@import url('https://fonts.googleapis.com/css2?family=Roboto+Condensed:wght@700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Roboto+Condensed&display=swap');
</style>
</head>

<body>
  <div id="header">
    
    <div class="left">
      <div class="space"></div>
       <div class="space"></div>
      <div><text class="gradient-text">MOJA SUPER STRONA</text></div>
      <div class="space"></div>
      <div class="clock">
        <script type = "text/javascript">
          function dzien()
          {
              var today = new Date();
              var d_week = today.getDay();
          
              document.getElementById("day").innerHTML = d_week + " dzień tygodnia";           
              setTimeout("dzien()", 1000); 
          }
          
          function czas()
          {
              var today = new Date();
              var h = today.getHours();
              var m = today.getMinutes();
              var s = today.getSeconds();
              if(m<10) m = "0" + m;
              if(s<10) s = "0" + s;
                      
                      
              document.getElementById("timer").innerHTML = h + ":" + m + "," + s;
              setTimeout("czas()", 1000);            
          }
  
          function date()
          {
              var today = new Date();                    
                      
              document.getElementById("date").innerHTML = today;
              setTimeout("date()", 1000);            
          }
  
          window.addEventListener('load', dzien, false);
          window.addEventListener('load', czas, false);
          window.addEventListener('load', date, false);
        </script>
      <table bgcolor="transparent">
          <tr>
              <td>
                  <font color="white" size="9">
                      <div id="day"></div>
                      <div id="timer"></div>
                  </font>
              </td>
          </tr>
      </table>
    </div>  
    </div>
    
    <div class="right">
      <div class="space"></div>
      <div class="space"></div>

     <center> <img src="emotka.png" height="230"></center>
    </div>


  </div>

  <div id="menu">
    <div class="space"></div>
    <button>
      <span class="button_top"><a id="przycisk" href="index.html"> Strona Główna </a></span>
    </button>
    <button>
      <span class="button_top"><a id="przycisk" href="prank.html"> Taki Żarcik </a></span>
    </button>
    <button>
      <span class="button_top"><a id="przycisk" href="konto.html"> Baza Danych </a></span>
    </button>
    <button>
      <span class="button_top"><a id="przycisk" href="sklep.html"> Sklep </a></span>
    </button>
    <div class="space"></div>
  </div>
    <div id="content">
        <div class="content">
            <div class="space"></div>
            <h1>Koszyk</h1>
              <?php
                // cena produktu
                $cena_proc1 = 300;
                $cena_proc2 = 800;
                $cena_proc3 = 1300;
                $cena_proc4 = 2000;

                $cena_graf1 = 700;
                $cena_graf2 = 1500;
                $cena_graf3 = 2500;
                $cena_graf4 = 4000;

                $cena_dysk1 = 200;
                $cena_dysk2 = 80;
                $cena_dysk3 = 160;
                $cena_dysk4 = 250;

                // ilość produktu
                $ilosc_proc1 = $_POST['ilosc_proc1'];
                $ilosc_proc2 = $_POST['ilosc_proc2'];
                $ilosc_proc3 = $_POST['ilosc_proc3'];
                $ilosc_proc4 = $_POST['ilosc_proc4'];
                
                $ilosc_graf1 = $_POST['ilosc_graf1'];
                $ilosc_graf2 = $_POST['ilosc_graf2'];
                $ilosc_graf3 = $_POST['ilosc_graf3'];
                $ilosc_graf4 = $_POST['ilosc_graf4'];

                $ilosc_dysk1 = $_POST['ilosc_dysk1'];
                $ilosc_dysk2 = $_POST['ilosc_dysk2'];
                $ilosc_dysk3 = $_POST['ilosc_dysk3'];
                $ilosc_dysk4 = $_POST['ilosc_dysk4'];

                // obliczanie ceny
                $cena_calkowita = $cena_proc1*$ilosc_proc1 + $cena_proc2*$ilosc_proc2 + $cena_proc3*$ilosc_proc3 + $cena_proc4*$ilosc_proc4 + $cena_graf1*$ilosc_graf1 + $cena_graf2*$ilosc_graf2 + $cena_graf3*$ilosc_graf3 + $cena_graf4*$ilosc_graf4 + $cena_dysk1*$ilosc_dysk1 + $cena_dysk2*$ilosc_dysk2 + $cena_dysk3*$ilosc_dysk3 + $cena_dysk4*$ilosc_dysk4;

                // wyświetlanie wyniku
                echo "<h2>Cena za twoje zakupy sztuk wynosi: $cena_calkowita zł.</h2>";
	        ?>
        </div>
    </div>
  
  <div id="footer">
    <div id="icons">
      <a class="link" href="https://www.facebook.com" target="_blank"> <i class="demo-icon icon-facebook-squared"></i></a>
      <a class="link" href="https://www.instagram.com" target="_blank"> <i class="demo-icon icon-instagram"></i></a>
      <a class="link" href="https://www.youtube.com" target="_blank"> <i class="demo-icon icon-youtube-play"></i></a>
            </div>
  Copyright &copy; 2023 Michał Lampara
  </div>
</body>

</html>