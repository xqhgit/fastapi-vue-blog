<template>
  <div>
    <div id="exampleModal" class="modal fade" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 id="exampleModalLabel" class="modal-title">New message</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <form>
              <div class="form-group">
                <label for="recipient-name" class="col-form-label">Recipient:</label>
                <input id="recipient-name" type="text" class="form-control">
              </div>
              <div class="form-group">
                <label for="message-text" class="col-form-label">Message:</label>
                <textarea id="message-text" class="form-control"/>
              </div>
            </form>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            <button type="button" class="btn btn-primary">Send message</button>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-md-8">
        <div id="main">
          <div class="post">
            <p class="date">January 11 2021</p>
            <h1 class="post-title">
              <a href="#">
                Beautiful Interactive Tables for your Flask Templates
              </a>
            </h1>
            <div class="posted">
              <span>类别：</span>
              <b-badge variant="info">Python</b-badge>,
              <b-badge variant="info">JavaScript</b-badge>.
            </div>
            <div class="post_body">
              Rendering a table with data in a Flask template is a relatively simple task when
              the table is short, but can be incredibly hard for larger tables that require
              features such as sorting, pagination and searching. In this article I'm going
              to show you how to integrate the dataTables.js library in your templates,
              which will allow you to create fully featured tables with ease!
            </div>
          </div>
          <div class="comment">
            <h5 style="text-align: right;">
              <span>4 个评论</span>
            </h5>
            <ul>
              <li>
                <div class="comment-body">
                  <div style="padding-top: 10px;" class="d-flex flex-row">
                    <b-badge variant="secondary">#1</b-badge>
                    <b-badge variant="info" style="margin: 0 4px;">demo</b-badge>
                    <span>2020-12-25T23:42:02Z</span>
                  </div>
                  <div style="overflow: auto;">
                    <p>Do you plan to make a paid guide/tutorial on this topic?  If not,do you have any resources that you'd recommend for a beginner, besides your videos?</p>
                  </div>
                  <div class="can-reply d-flex flex-row-reverse">
                    <b-button type="button" size="sm" variant="outline-secondary">回复</b-button>
                  </div>
                </div>
              </li>
              <li>
                <div class="comment-body">
                  <div style="padding-top: 10px;" class="d-flex flex-row">
                    <b-badge variant="secondary">#2</b-badge>
                    <b-badge variant="danger" style="margin: 0 4px;">admin</b-badge>
                    <span>2020-12-25T23:42:02Z</span>
                  </div>
                  <div style="overflow: auto;">
                    <p style="margin-bottom: 0">@demo</p>
                    <p>Yes. I don't have a release date yet, but I'm working on a longer React tutorial.</p>
                  </div>
                </div>
              </li>
            </ul>
          </div>

          <h5>留下你的评论</h5>
          <b-form>
            <b-form-group id="input-group-1" label="你的名字:" label-for="input-1">
              <b-form-input
                id="input-1"
                required
              />
            </b-form-group>
            <b-form-group
              id="input-group-2"
              label="电子邮箱:"
              label-for="input-2"
            >
              <b-form-input
                id="input-2"
                type="email"
                required
              />
            </b-form-group>
            <b-form-group
              id="input-group-3"
              label="评论:"
              label-for="input-3"
            >
              <b-form-textarea
                id="input-3"
                required
                style="height: 150px;"
              />
            </b-form-group>
          </b-form>
          <b-button type="submit" variant="outline-secondary">提交</b-button>
        </div>
      </div>
      <div class="col-md-4 category-sidebar-bg">
        <category-sidebar />
      </div>
    </div>
  </div>
</template>

<script>
import CategorySidebar from '@/components/CategorySidebar'

export default {
  name: 'PostPageIndex',
  components: { CategorySidebar }
}
</script>

<style scoped>
    #main {
    padding: 10px 10px 10px 10px;
  }

  #main .date {
    padding: 2px 8px;
    margin: 5px 0px 0px 0px;
    border: 1px solid #ccc;
    font-size: 100%;
    color: #666;
    float: right;
    display: inline;
    position: relative;
    top: 4px;
  }
  #main h1 {
    font-size: 170%;
    font-weight: normal;
    line-height: 140%;
    padding-bottom: 5px;
    margin-top: 20px;
  }

  #main p {
    font-size: 120%;
    line-height: 150%;
    margin-bottom: 20px;
  }
  #main .post {
    margin-bottom: 20px;
    /*border-bottom: 1px solid #ccc;*/
  }
  #main h1.post-title a {
    color: #666;
    cursor:pointer;
    text-decoration:none;
  }
  #main h1.post-title a:hover {
    color: black;
  }
  #main .posted {
    font-size: 100%;
    font-weight: normal;
    padding-bottom: 4px;
    margin-bottom: 16px;
    border-bottom: 1px solid #ccc;
  }

  .category-sidebar-bg {
    background-color: #f0f0f0;
    margin-top: 10px;
    height: 100%;
    padding-bottom: 16px;
    padding-top: 16px;
  }

  #main .comment {
    padding: 4px 4px 8px 4px;
    /*border-top: 1px solid #ddd;*/
    font-size: 80%;
  }
  #main .comment ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
  }
  #main .comment ul li {
    padding: 8px;
  }
  #main .comment ul li:nth-child(odd) {
    background-color: #eee;
    border-bottom: 1px solid #ddd;
  }
  #main .comment ul li div.comment-thumbnail {
    width: 60px;
    position: absolute;
  }
  #main .comment ul li div.comment-body {
    /*margin-left: 70px;*/
    overflow: auto;
  }
</style>
