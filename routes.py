from flask import Blueprint, redirect, render_template, request
from init import db
from models import Post, PostTag, Tag, User

app_routes = Blueprint("app_routes", __name__, static_folder='static', static_url_path='/app_routs/stati', template_folder='templates')


@app_routes.route("/")
def home():
    return redirect("/users")


@app_routes.route("/users")
def show_users():
    users = db.session.execute(
        db.select(User).order_by(User.first_name, User.last_name)
    ).scalars()
    return render_template("home.html", users=users)


@app_routes.route("/users/<user_id>")
def user_profile(user_id):
    user = db.session.execute(db.select(User).where(User.id == user_id)).scalar_one()
    return render_template("user_profile.html", user=user)


@app_routes.route("/users/new", methods=["GET", "POST"])
def new_user():
    if request.method == "POST":
        user = User(
            first_name=request.form["first_name"],
            last_name=request.form["last_name"],
            image_url=request.form["image_url"],
        )
        user.image_url = user.image_url if user.image_url else None

        db.session.add(user)
        db.session.commit()
        return redirect("/users")
    return render_template("add_user.html")


@app_routes.route("/users/<user_id>/edit", methods=["GET", "POST"])
def edit_profile_user(user_id):
    user = db.session.execute(db.select(User).filter_by(id=user_id)).scalar_one()

    if request.method == "POST":
        user.first_name = request.form["first_name"]
        user.last_name = request.form["last_name"]
        user.image_url = request.form["image_url"]

        db.session.add(user)
        db.session.commit()
        return redirect(f"/users/{user.id}")

    return render_template("edit_profile.html", user=user)


@app_routes.route("/users/<user_id>/delete")
def delete_profile_user(user_id):
    user = db.session.execute(db.select(User).filter_by(id=user_id)).scalar_one()
    db.session.delete(user)
    db.session.commit()
    return redirect("/users")


@app_routes.route("/users/<user_id>/posts/new", methods=["GET", "POST"])
def add_new_post(user_id):
    tags = db.session.execute(db.select(Tag)).scalars()
    if request.method == "POST":
        post = Post(
            title=request.form["title"],
            content=request.form["content"],
            user_id=user_id,
        )
        db.session.add(post)
        db.session.commit()
        posttag = []
        for tag in request.form.getlist('tags'):
            posttag.append(
                PostTag(
                    post_id= post.id,
                    tag_id= tag
                )
            )
        db.session.add_all(posttag)
        db.session.commit()

            
        return redirect(f"/users/{user_id}")
    return render_template("add_new_post.html", user_id=user_id, tags=tags)


@app_routes.route("/posts/<post_id>")
def show_post(post_id):
    post = db.session.execute(db.select(Post).filter_by(id=post_id)).scalar_one()
    return render_template("post.html", post=post)


@app_routes.route("/posts/<post_id>/edit", methods=["GET", "POST"])
def edit_post(post_id):
    post = db.session.execute(db.select(Post).filter_by(id=post_id)).scalar_one()
    tags = db.session.execute(db.select(Tag)).scalars()
    posttag = db.session.execute(db.select(PostTag).join(Post).where(PostTag.post_id == post.id)).scalars()
    if request.method == "POST":
        post.title = request.form["title"]
        post.content = request.form["content"]

        db.session.add(post)
        db.session.commit()
        return redirect(f"/posts/{post.id}")
    return render_template("edit_post.html", post=post, tags=tags, posttag=list(posttag))


@app_routes.route("/posts/<post_id>/delete")
def delete_post(post_id):
    post = db.session.execute(db.select(Post).filter_by(id=post_id)).scalar_one()
    user_id = post.user.id
    db.session.delete(post)
    db.session.commit()
    return redirect(f"/users/{user_id}")

@app_routes.route('/tags')
def tag_list():
    tags = db.session.execute(db.select(Tag)).scalars()
    return render_template('tags.html', tags=tags)


@app_routes.route('/tags/new', methods=['GET', 'POST'])
def create_new_tag():
    if request.method == 'POST':
        print(request.form['name'])
        tag = Tag(
            name = request.form['name']
        )
        db.session.add(tag)
        db.session.commit()
        return redirect('/tags')
    return render_template('add_tag.html')

@app_routes.route('/tags/<tag_id>')
def show_tag(tag_id):
    tag = db.session.execute(db.select(Tag).where(Tag.id == tag_id)).scalar_one()
    return render_template('tag.html', tag=tag)


@app_routes.route('/tags/<tag_id>/edit', methods=['GET', 'POST'])
def edit_tag(tag_id):
    tag = db.session.execute(db.select(Tag).where(Tag.id == tag_id)).scalar_one()
    if request.method == 'POST':
        tag.name = request.form['name']
        db.session.add(tag)
        db.session.commit()
        return redirect(f'/tags/{tag.id}')
    return render_template('edit_tag.html', tag=tag)


@app_routes.route('/tags/<tag_id>/delete')
def delete_tag(tag_id):
    tag = db.session.execute(db.select(Tag).where(Tag.id == tag_id)).scalar_one()
    db.session.delete(tag)
    db.session.commit()
    return redirect('/tags') 
