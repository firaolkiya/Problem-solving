!function(){const t=document.querySelector('a[href^="/profile/"]');if(t){const e=t.textContent.trim(),n=window.location.href.split("/");""==n[n.length-1]&&n.pop();const o=n[n.length-1];chrome.runtime.sendMessage({type:"fromContent",data:{username:e,currContestID:o}})}}();