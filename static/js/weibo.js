$(document).ready(function() {
  $('#tong-weibo-block').on('click', '.tong-weibo-edit', function () {
    var weiboId = $(this).data('id')
    var selector = "#id-form-edit-" + weiboId
    $(selector).slideToggle('.tong-hide')
  })

  $('#tong-weibo-block').on('click', '.tong-weibo-comment', function () {
    var weiboId = $(this).data('id')
    var selector = "#id-div-comment-" + weiboId
    $(selector).slideToggle('.tong-hide')
    console.log(weiboId)
  })
})
