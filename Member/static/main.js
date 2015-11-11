
var ptr = 1;
var bound = $('.product_list').length;
window.onload = function (){

 $('.product_list').hide();
 name = makeName(ptr);
 $(name).show();
 checkBound();
}



function previous(){
 
 $(makeName(ptr)).hide();
 ptr = ptr -1 ;
 checkBound();
 $(makeName(ptr)).show();

}


function next(){
 
 $(makeName(ptr)).hide();
 ptr = ptr +1 ;
 checkBound();
 $(makeName(ptr)).show();

}


function makeName(count){

	return '#product' + count;

}
function checkBound(){
	
	if (ptr == bound){
		$('#next_btn').hide();
	}
	else{
	$('#next_btn').show();
	}

	if(ptr == 1){
		$('#pre_btn').hide();
	}
	else{
		$('#pre_btn').show();
	}
}
