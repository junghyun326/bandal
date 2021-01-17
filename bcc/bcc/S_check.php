<?php
	$conn = mysqli_connect("bcc-database.cxmkpfyh3g9z.ap-northeast-2.rds.amazonaws.com","jeonghyun","bcc416416","bcc-schema");
	$result = mysqli_query($conn,"SELECT * FROM professor");
?>

<!doctype html>
<html>
<head>
	<meta charset="utf-8">
	<title>BCC</title>
<link href="style.css" rel="stylesheet" type="text/css">
<style type="text/css">
body {
    background-image: url(image/background_orange.png);
    background-repeat: repeat-x;
    background-color: #F6CE45;
}
a:link {
    color: #000000;
    text-decoration: none;
}
a:visited {
    text-decoration: none;
    color: #000000;
}
a:hover {
    text-decoration: none;
    color: #F69A2D;
}
a:active {
    text-decoration: none;
    color: #000000;
}
table {
        width: 100%;
        font-size: 8pt;
      }
th {
        padding: 10px;
        border-bottom: 1px solid #dadada;
        border-color: #F6CE45;
      }
td {
      padding: 10px;
      border-bottom: 1px solid #dadada;
}
</style>
</head>


<body>
<header class="header_top">
	  <div class="header_logo" onmouseover="messageWindow()"><a href = "http://bcc.iptime.org/bcc/index.php"><img src="image/bcc_logo_yellow_2.png" width="130" height="132" alt="" /></a></div>
	  <div class="header_textlogo"><a href = "http://bcc.iptime.org/bcc/index.php"><img src="image/bcc_title_yellow.png" width="100" height="49" alt=""/></a></div>
	</header>

	<main class="main_section" style="width: 1000px; margin-left: auto; margin-right: auto; border-top-left-radius: 30px;
  border-left: 3px solid #F69A2D; border-right: 3px solid #F69A2D; border-bottom: 3px solid #F69A2D; border-top: 3px solid #F69A2D;
  border-top-right-radius: 30px; height: 1000px; margin-top: 10px; background-color: #FFFFFF;">
	  <section class="main_div">
	    <a href = "http://bcc.iptime.org/bcc/index.php">
        <img src="image/left-arrow.png" width="50" height="51" margin_left="5px" alt=""/>
      </a>
    </section>

	  <section class="main_body">
		  <article class="action_main_body_2_t" style="height: 30px; width: 970px; float: left; padding-left: 30px;
      padding-top: 10px;   padding-bottom: 10px; background-color: #F6CE45; border-bottom: medium double #F69A2D;">
      <img src="image/register.png" alt="" width="30" float = left/>
      <?php
      $sql_2 = 'SELECT subname FROM subject WHERE subnum='.$_POST['s_num'];
      $result_2 = mysqli_query($conn,$sql_2);
      $row_2 = mysqli_fetch_assoc($result_2);
      echo $row_2['subname'].' 수업 - '; // 들어온 과목이름 출력

      $sql_3 = 'SELECT pname FROM professor WHERE pnum='.$_POST['p_num'];
      $result_3 = mysqli_query($conn,$sql_3);
      $row_3 = mysqli_fetch_assoc($result_3);
      echo $row_3['pname'].' 교수님'; //들어온 교수번호로 교수이름 출력
       ?>
			</article>

		<article class="action_main_body_2_b">

        <table>
        <thead>
          <tr>
            <th>이름</th> <th>1주차</th> <th>2주차</th> <th>3주차</th> <th>4주차</th> <th>5주차</th> <th>6주차</th> <th>7주차</th> <th>8주차</th>
            <th>9주차</th> <th>10주차</th> <th>11주차</th> <th>12주차</th> <th>13주차</th> <th>14주차</th> <th>15주차</th> <th>16주차</th>
          </tr>
        </thead>
          <tbody>
            <?php
              $sql_4 = 'SELECT * FROM enroll , student WHERE enroll.sid=student.sid and subnum='.$_POST['s_num']; // 등록이랑 학생 테이블 조인해서 읽어오기
              $result_4 = mysqli_query($conn,$sql_4);

              while( $row_4 = mysqli_fetch_array( $result_4 ) ) {
                echo '<tr><td>' . $row_4[ 'sname' ] .'</td><td>'. $row_4[ 'w01' ] .'</td><td>'. $row_4[ 'w02' ] .'</td><td>'. $row_4[ 'w03' ] .'</td><td>'.  $row_4[ 'w04' ] .'</td><td>'. $row_4[ 'w05' ]
                                .'</td><td>'. $row_4[ 'w06' ] .'</td><td>'. $row_4[ 'w07' ] .'</td><td>'. $row_4[ 'w08' ] . '</td><td>'. $row_4[ 'w09' ] .'</td><td>'. $row_4[ 'w10' ]
                                .'</td><td>'. $row_4[ 'w11' ] .'</td><td>'. $row_4[ 'w12' ] .'</td><td>'. $row_4[ 'w13' ] .'</td><td>'.  $row_4[ 'w14' ] .'</td><td>'. $row_4[ 'w15' ] .'</td><td>'. $row_4[ 'w16' ] .'</td><tr>';
                                      }
            ?>
          </tbody>
        </table>
		  </article>
      <article class="action_main_body_button">
        <form action="http://bcc.iptime.org/bcc/r_check.php" method="POST">
				  <p><input type="image" src="image/button.png" width="100" height="27"/></p>
			  </form>
      </article>
		</section>
	</main>
</body>
</html>
