(()=>{var t={37:t=>{t.exports={getContests:async function(){try{const t=await fetch("https://a2sv-contest-monitoring-system.onrender.com/api/v1/contests");return await t.json()}catch(t){throw console.error("Error fetching contests:",t),t}},getActiveContest:async function(){try{const t=await fetch("https://a2sv-contest-monitoring-system.onrender.com/api/v1/contests?active=true");return await t.json()}catch(t){throw console.error("Error fetching active contests:",t),t}}}}},o={};!function r(e){var n=o[e];if(void 0!==n)return n.exports;var s=o[e]={exports:{}};return t[e](s,s.exports,r),s.exports}(37)})();