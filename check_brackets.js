function checkBrackets(string) {
 brackets = 0
	for (let i = 0; i < string.length; i++) {
    if (string.charAt(i) == '('){
        brackets++   
    }
    if (string.charAt(i) == ')') {
    brackets--
    }
	}
	if (brackets == 0) {
	return 'valid'
    }
	else {
  	return 'not valid'}
}
console.log(checkBrackets('(((()))'))
