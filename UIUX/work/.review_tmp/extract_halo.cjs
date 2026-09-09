const fs=require('fs'),path=require('path'),vm=require('vm');
const base=path.join(__dirname,'..','박찬미','웹사이트','와이어프레임');
const main=fs.readFileSync(path.join(base,'와이어프레임_시안5_최종.html'),'utf8');
const cat=fs.readFileSync(path.join(base,'카테고리_시안2.html'),'utf8');
const extract=(s,name)=>{const m=s.match(new RegExp('const '+name+' = ([\\s\\S]*?);')); if(!m)throw Error(name);return vm.runInNewContext('('+m[1]+')');};
const data={skus:extract(cat,'skuMasterList'),scenes:extract(main,'sceneData'),quick:extract(main,'skuMasterDict'),colMeta:extract(cat,'colMeta')};
fs.writeFileSync(path.join(__dirname,'halo-data.json'),JSON.stringify(data,null,2));
console.log('Extracted',data.skus.length,'products;',Object.keys(data.scenes).length,'collection states');
