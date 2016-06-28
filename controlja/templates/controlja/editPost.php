<!DOCTYPE html>
<html>
	<head>
		<title>Nueva Entrada</title>
		<link type="text/css" rel="stylesheet" href="style.css" media="all">
	</head>
	<body>

		<?php
			/*ini_set('display_errors', 1);
			error_reporting(E_ALL);*/
		
			require_once(__DIR__.'/models/Post.php');
		
			$ins = new Post();
			$posts = $ins->getPost( $_GET['id'] );
		?>
		
		<div id="newPostPanel">
			<h1>Editar entrada</h1>
			<form id="form1" action="listeners/EditPost.php" method="post">
				<input type="hidden" name="id" value="<?=$_GET['id']?>"></input>
				<div class="salto2">
					<span>T&iacute;tulo</span><br/>
					<input type="text" name="title" value="<?=$posts['title']?>"></input>
				</div>
				<div class="salto2">
					<span>Contenido</span><br class="salto1"/>
					<textarea name="content" form="form1"><?=$posts['content']?></textarea><br class="salto3"/>
				</div>
				<button class="button" onclick="this.submit();">Subir!</button>
			</form>
			<a href="/" class="button"><< al blog</a>
		</div>
	</body>
</html>
