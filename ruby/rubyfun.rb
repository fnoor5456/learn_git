puts 'Hello, what number do you want me to count to? '

$i = 1
$num = gets.chomp.to_i

begin 
	puts("#$i")
	$i += 1
end while $i <= $num
