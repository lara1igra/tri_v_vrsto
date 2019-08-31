<!DOCTYPE html>
<html>
<style>
	td {
		border: 1px solid black;
		height: 100px;
		width: 100px;
	}
</style>
<body>  
    <h1>Tri v vrsto</h1>
	
	%polje11=trivvrsto.seznam[0]
	%polje12=trivvrsto.seznam[1]
	%polje13=trivvrsto.seznam[2]
	%polje21=trivvrsto.seznam[3]
	%polje22=trivvrsto.seznam[4]
	%polje23=trivvrsto.seznam[5]
	%polje31=trivvrsto.seznam[6]
	%polje32=trivvrsto.seznam[7]
	%polje33=trivvrsto.seznam[8]
	
	<table>
		<tr>
			<td>1,1<img src="../img/{{polje11}}.png"/></td>
			<td>1,2<img src="../img/{{polje12}}.png"/></td>
			<td>1,3<img src="../img/{{polje13}}.png"/></td>
		</tr>
		<tr>
			<td>2,1<img src="../img/{{polje21}}.png"/></td>
			<td>2,2<img src="../img/{{polje22}}.png"/></td>
			<td>2,3<img src="../img/{{polje23}}.png"/></td>
		</tr>
		<tr>
			<td>3,1<img src="../img/{{polje31}}.png"/></td>
			<td>3,2<img src="../img/{{polje32}}.png"/></td>
			<td>3,3<img src="../img/{{polje33}}.png"/></td>
		</tr>
	</table>

	<h1>
    {{text}}
    </h1>

    <form action="" method="post">
        Vnesi stolpec in vrstico (npr.: 1,3): <input type="text" name="vrsticaStolpec">
        <input type="submit" value="Potrdi izbiro">
    </form><br>

</body>
<footer>
    <form action="/nova_igra/" method="post">
        <button type="submit">Nova igra</button>
    </form>
</footer>

</html>