<?php
	$conn = mysqli_connect("bcc-database.cxmkpfyh3g9z.ap-northeast-2.rds.amazonaws.com","jeonghyun","bcc416416","bcc-schema");
	$result = mysqli_query($conn,"SELECT * FROM professor");
	$id = '';
	$pw = '';
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

ol {
    display: block;
    list-style-type: decimal;
    margin-block-start: 1em;
    margin-block-end: 1em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
    padding-inline-start: 10px;
}

ul {
		list-style-type: square;
    padding-inline-start: 20px;
}

</style>
<link rel="shortcut icon" href="favicon.ico">
<link rel="icon" href="favicon.ico">
</head>
<body>
	<header class="header_top">
	  <div class="header_logo" onmouseover="messageWindow()"><a href = "http://bcc.iptime.org/bcc/index.php"><img src="image/bcc_logo_yellow.png" width="130" height="132" alt="" /></div>
	  <div class="header_textlogo"><img src="image/bcc_title_yellow.png" width="100" height="49" alt=""/></a></div>
	</header>

	<main class="main_section" style="width: 1000px; margin-left: auto; margin-right: auto; border-top-left-radius:
	30px; border-left: 3px solid #F69A2D; border-right: 3px solid #F69A2D; border-bottom: 3px solid #F69A2D;
	border-top: 3px solid #F69A2D; border-top-right-radius: 30px; height: 1000px; margin-top: 10px; background-color: #FFFFFF;">
	  <section class="main_div"></section>

	  <section class="main_body">
		  <article class="action_main_body">
				<?php
				if(empty($_GET['id'])===false){ //id값이 있을때만 돌아간다(안그럼 메인에서 오류)
					$sql = 'SELECT * FROM subject WHERE pnum='.$_GET['id']; //과목중에 해당 pnum인 행 고름(id=교번)
					$result_1 = mysqli_query($conn,$sql);
					while($row = mysqli_fetch_assoc($result_1)){ //과목이 여러개 일 수 있으니까 돌려줌
						echo '<h1>'.$row['subname'].'(과목코드 : '.$row['subnum'].')'.'</h1>'; //과목이름을 출력
						//로그인 기능
						$id_row = mysqli_fetch_assoc(mysqli_query($conn,'SELECT * FROM subject WHERE pnum='.$_GET['id']));
						$pw_row = mysqli_fetch_assoc(mysqli_query($conn,'SELECT * FROM subject WHERE pnum='.$_GET['id']));
						$id = $id_row['subnum'];
						$pw = $id_row['pnum'];
					}
				} else {
					echo '<h1>'.'사용자의 이름을 선택해주세요 :)'.'</h1>';
				}


				?>
			</article>
			<article class="action_main_body">
			  <form action="http://bcc.iptime.org/bcc/s_check.php" method="POST">
					<p><input type="text" name="s_num" placeholder="과목코드"></p>
				  <p><input type="password" name="p_num" placeholder="비밀번호"></p>
				  <p><input type="submit" title="시작"/></p>
			  </form>
		  </article>
		</section>
	  <section class="main_right_section">
	    <nav class="right_nav">
				<ol>
					<ul>
						<?php
							while($row = mysqli_fetch_assoc($result)){ //여러개니까 있는거 다 돌려줌
								echo '<li><a href = "http://bcc.iptime.org/bcc/index.php?id='.$row['pnum'].'" text-decoration= none>'.$row['pname'].'교수님'.'</a></li>';
								//리스트마다 링크를 걸어주는데 아이디를 교번으로 걸어줌
								echo "<br/>";
							}
						?>
					</ul>
		  </nav>
	  </section>
	</main>
</body>
</html>
