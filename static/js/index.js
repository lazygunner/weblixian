var DownloadStatus = function()
	{
	var that = this;
	var registerError = function(XMLHttpRequest, textStatus, errorThrown)
		{
			//$("#results").append("<li class='error'>Error:" + textStatus + "</li>");
			$("#button").removeAttr("disabled");
		};
	var registerSuccess = function(data, textStatus, XMLHttpRequest)
		{
		 try
		 		{
		 			if(data == '')
		 				return;
		 			var downloadStatus = JSON.parse(data)
		 			var per = downloadStatus.per;
		 			var speed = downloadStatus.speed;
		 			var eta = downloadStatus.eta;
		 			var ok = downloadStatus.ok;
		 			//$("#results").append("<li class='sucesss'>Estimated clock skew :<span class='measurement'>" + per + "</span> seconds.</li>");
		 			//$("#results").append("<li class='sucesss'>Downloaded :<span class='measurement'>" + per + "</span>%.</li>");
		 			var perString = per + '%';
		 			$(".bar").css("width", perString);
		 			$("#perCon").text(perString);
		 			$("#speed").text("下载速度:" + speed);
		 			$("#eta").text("剩余时间:" + eta);
		 			if(ok == 0)		 				
						DownloadStatus.buttonDownPress();
					else if(ok == 1){
						$(".downloadLinks").first().remove();
						Download.buttonPress();
					}
					else if(ok == 2){
						$(".downloadLinks").first().remove();
					}
					else							
						return;
		 		}
		 	catch(error)
		 		{
		 			$("#results").append("<li class='error'>Error parsing JSON.</li>");
		 			DownloadStatus.buttonDownPress();
		 		}
		 	$("#button").removeAttr("disabled");
		 	
		};
		
	var buttonDownPress = function()
		{

		$.ajax({data:"", dataType:"text", error: registerError, 
			success: registerSuccess, type: "POST",
			url: "/check/"});
		};
	
	return {
		buttonDownPress: buttonDownPress
		}
	}();
var check_delay = function(){
	
	
	
	
};

var Download = function(){
		var that = this;
		var registerError = function(XMLHttpRequset, textStatus, errorThrown)
		{

		};
		var registerSuccess = function(data, rextStatus, XMLHttpRequest)
		{
				if(data == "redown"){
					alert("已在下载列表！");
					return;
				}
				$("#linkList").append("<li class=\"downloadLinks\">" + data + "</li>")
				DownloadStatus.buttonDownPress();
		};
		
		var buttonPress = function()
		{
			var downloadLink = {'link':$("#link").val()};
			$("#link").val('');
			
			$.ajax({data:downloadLink, datraType:"text", error: registerError,
					success: registerSuccess, tyep: "POST", url:"/download/"});
		};
		
		return{
			buttonPress : buttonPress
		}
			
	
}();



$(document).ready(function() {
	//var d = new Download();
	//var s = new DownloadStatus();
	$("#download").click(Download.buttonPress);
	DownloadStatus.buttonDownPress();
//	$("#download").click(MeasureClockSkew.buttonPress);
//	$("#button").click(test);
});