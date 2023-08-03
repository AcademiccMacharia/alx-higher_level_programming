$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data, textStatus) {
  console.log(data)
  $('DIV#hello').text(data.hello);
});
