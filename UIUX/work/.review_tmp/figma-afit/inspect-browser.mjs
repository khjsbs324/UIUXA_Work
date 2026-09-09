const port=process.argv[2]||9224;
const tabs=await (await fetch(`http://127.0.0.1:${port}/json`)).json();
const tab=tabs.find(t=>t.type==='page');
const ws=new WebSocket(tab.webSocketDebuggerUrl);
await new Promise(r=>ws.addEventListener('open',r,{once:true}));
let id=0;
function command(method,params={}){return new Promise((resolve,reject)=>{const req=++id;const on=e=>{const msg=JSON.parse(e.data);if(msg.id===req){ws.removeEventListener('message',on);resolve(msg)}};ws.addEventListener('message',on);ws.send(JSON.stringify({id:req,method,params}));setTimeout(()=>reject(new Error('CDP timeout')),15000).unref()})}
const expression=process.argv[3]||`JSON.stringify({title:document.title,ready:document.readyState,body:document.body?.innerText.slice(-1500),figma:typeof window.figma,resources:performance.getEntriesByType('resource').map(e=>({name:e.name,duration:e.duration,size:e.transferSize})),url:location.href})`;
if(process.argv[3]==='navigate')console.log(JSON.stringify(await command('Page.navigate',{url:process.argv[4]||tab.url}),null,2));
else console.log(JSON.stringify(await command('Runtime.evaluate',{expression,returnByValue:true}),null,2));
ws.close();
