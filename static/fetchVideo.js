

function fetchVideo(){
  document.getElementById("video-details").style.opacity = 1;
   let str = String(document.getElementById("fetch-video-url").value);
   if(str.includes("youtu.be")){

     let url1 = str.substr(17);
     console.log(url1)
     let src = document.getElementsByClassName("thumbs").src;
     console.log(src);
     document.getElementsByClassName("thumbs").src = str;
     let s1 = "https://www.youtube.com/embed/".concat(url1);
     src = document.getElementsByClassName("thumbs").src = s1;
     console.log(src);
     let url2 = "https://www.googleapis.com/youtube/v3/videos?key=AIzaSyA6VX3z31ObjBXhbr0JYMwfuftGGqivgaY&part=snippet&id=";
     let url = url2.concat(url1);
     
     fetch(url).then((response) => {
       return response.json();
     }).then((data) => {
       console.log(data)
       console.log(data.items[0].snippet.description);
       document.getElementById("video-title").innerHTML = data.items[0].snippet.title;
       // document.getElementById("video-desc").innerHTML = data.items[0].snippet.description;
       $(".thumbs").attr('src', data.items[0].snippet.thumbnails.high.url)
       console.log(data.items[0].snippet.title);
       
       document.getElementById("video_title").value = data.items[0].snippet.title;
       document.getElementById("video_thumbnail").value = data.items[0].snippet.thumbnails.high.url;
       document.getElementById("video_platform_id").value = url1;
     })
   }
   else if(str.includes("dailymotion")){
     let url1 = str.substr(34);
     console.log(url1);
     let url2 = "https://api.dailymotion.com/video/"
     let url = url2.concat(url1);
     fetch(url).then((response) => {
       return response.json();
     }).then((data) => {
       console.log(data)
       console.log(data.title);
       document.getElementById("video-title").innerHTML = data.title;
       // document.getElementById("video-desc").innerHTML = data.items[0].snippet.description;
       $(".thumbs").attr('src', 'https://dailymotion.com/thumbnail/video/' + url1);
       
       document.getElementById("video_title").value = data.title;
       document.getElementById("video_thumbnail").value = 'https://dailymotion.com/thumbnail/video/' + url1;
       document.getElementById("video_platform_id").value = url1;

     })
   }
  else {
       let id = str.substr(18);
       $.getJSON('https://vimeo.com/api/oembed.json?url=https://vimeo.com/' + id, {format: "json"}, function(data) {
         $(".thumbs").attr('src', data.thumbnail_url)
         document.getElementById("video-title").innerHTML = data.title;
       document.getElementById("video_title").value = data.title;
       document.getElementById("video_thumbnail").value = data.thumbnail_url;
       document.getElementById("video_platform_id").value = id;
       });
   }
 }
