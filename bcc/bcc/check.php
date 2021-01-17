<?php
	$conn = mysqli_connect("bcc-database.cxmkpfyh3g9z.ap-northeast-2.rds.amazonaws.com","jeonghyun","bcc416416","bcc-schema");
	$result = mysqli_query($conn,"SELECT * FROM professor");
?>

<!doctype html>
<html>
<head>
	<meta charset="utf-8">
	<title>index</title>
<link href="style.css" rel="stylesheet" type="text/css">
<style type="text/css">
body {
    background-image: url(image/background_orange.png);
    background-repeat: repeat-x;
    background-color: #F6CE45;
}
</style>
</head>
	<script type="text/javascript" src="../../Downloads/2016111584/2016111584/bcc_script.js"></script>


<body>
	<header class="header_top">
	  <div class="header_logo" onmouseover="messageWindow()"><img src="image/bcc_logo_yellow.png" width="130" height="132" alt="" /></div>
	  <div class="header_textlogo"><img src="image/bcc_title_yellow.png" width="100" height="49" alt=""/></div>
	</header>

	<main class="main_section" style="width: 1000px; margin-left: auto; margin-right: auto; border-top-left-radius: 30px;
	border-left: 3px solid #F69A2D; border-right: 3px solid #F69A2D; border-bottom: 3px solid #F69A2D; border-top: 3px solid #F69A2D;
	border-top-right-radius: 30px; height: 1000px; margin-top: 10px; background-color: #FFFFFF;">
	  <section class="main_div"></section>

	  <section class="main_body">
		  <article class="action_main_body">
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

			<article class="action_main_body2">
				<table>
					<tbody style="">
						<thread>
							<tr class="table_stl">
					      <th>학번</th>
								<th>이름</th>
								<th>1주차</th>
								<th>2주차</th>
								<th>3주차</th>
								<th>4주차</th>
								<th>5주차</th>
								<th>6주차</th>
								<th>7주차</th>
								<th>8주차</th>
								<th>9주차</th>
								<th>10주차</th>
								<th>11주차</th>
								<th>12주차</th>
								<th>13주차</th>
								<th>14주차</th>
								<th>15주차</th>
								<th>16주차</th>
			    		</tr>
						</thread>
			  	</tbody>
					<?php
					$sql_4 = 'SELECT * FROM enroll WHERE subnum='.$_POST['s_num']; //enroll 중 해당 수업의 테이블만 읽어오기
					$result_4 = mysqli_query($conn,$sql_4);

					while( $row_4 = mysqli_fetch_array( $result_4 ) ) {
	        echo '<p>' . $row_4[ 'sid' ] . $row_4[ 'w01' ] . $row_4[ 'w02' ] . $row_4[ 'w03' ] .  $row_4[ 'w04' ] . $row_4[ 'w05' ]
																		   . $row_4[ 'w06' ] . $row_4[ 'w07' ] . $row_4[ 'w08' ] .  $row_4[ 'w09' ] . $row_4[ 'w10' ]
																			 . $row_4[ 'w11' ] . $row_4[ 'w12' ] . $row_4[ 'w13' ] .  $row_4[ 'w14' ] . $row_4[ 'w15' ] . $row_4[ 'w16' ] .'</p>';
					}
					?>
				</table>
			</article>
			<img src="image/button.png" width="100" height="27" alt=""/>
		</section>
	</main>
</body>
</html>
