import os
from flask import Flask, render_template, url_for, flash, redirect, request, send_from_directory
from kwazar_website import app, db, bcrypt, mail
from kwazar_website.forms import LoginForm, PostForm, ContactForm
from kwazar_website.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message


@app.route("/")
def home():
    meta_desc = 'Realizujemy usługi takie jak pranie wykładzin, dywanów, tapicerki meblowej, czyszczenie kostki brukowej, mycie elewacji, posadzek... i wiele innych. Sprawdź nas!'
    return render_template('home.html', title='Profesjonalne Czyszczenie "Kwazar"', meta_desc=meta_desc, home=True)


@app.route("/o-firmie")
def o_firmie():
    meta_desc = 'Funkcjonujemy na rynku już od 2007r., realizujemy kompleksowe usługi czyszczenia na terenie Bydgoszczy i okolic. Sprawdź dlaczego tak wielu już nam zaufało!'
    return render_template('o-firmie.html', title='O Firmie', meta_desc=meta_desc)


@app.route("/aktualnosci")
def aktualnosci():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=4)
    return render_template('aktualnosci.html', title='Aktualności', posts=posts, aktualnosci=True)


@app.route("/uslugi")
def uslugi():
    meta_desc = 'Oferujemy pranie dywanów, tapicerki, czyszczenie kostki brukowej, posadzek... Obsługujemy zarówno Klientów Indywidualnych jak i Firmy. Sprawdź nasz pełen katalog usług!'
    return render_template('uslugi.html', title='Usługi', meta_desc=meta_desc)


@app.route("/uslugi/uslugi-ekspres")
def uslugi_ekspres():
    meta_desc = 'Wiemy, że w przypadku awarii należy działać szybko, doraźnie. Dlatego oferujemy czyszczenie i inne działania ograniczające ich skutki – sprawdź Usługi Ekspres!'
    return render_template('/uslugi/uslugi-ekspres.html', title='Usługi Ekspres', meta_desc=meta_desc)


@app.route("/uslugi/dla-domu")
def uslugi_dom():
    meta_desc = 'Pranie dywanów, tapicerki meblowej, czyszczenie kostki brukowej, podjazdów, dachów, mycie elewacji i wiele, wiele więcej. Rozgość się i wybierz usługę dla siebie!'
    return render_template('/uslugi/uslugi-dla-domu.html', title='Usługi dla Domu', meta_desc=meta_desc)


@app.route("/uslugi/dla-domu/mycie-konserwacja-dachow")
def dom_dachy():
    canonical = url_for('firma_dachy', _external=True)
    meta_desc = 'Na terenie Bydgoszczy i okolic oferujemy usługi z zakresu czyszczenia, konserwacji i malowania dachów. Odnawiamy powłoki malarskie. Sprawdź szczegóły naszej oferty!'
    return render_template('/uslugi/dla-domu/mycie-konserwacja-dachow.html', title='Czyszczenie, koserwacja i malowanie dachów', meta_desc=meta_desc, canonical=canonical)


@app.route("/uslugi/dla-domu/czyszczenie-kostki-brukowej")
def dom_kostka():
    canonical = url_for('firma_kostka', _external=True)
    meta_desc = 'Na terenie Bydgoszczy i okolic oferujemy usługi z zakresu czyszczenia i impregnacji kostki brukowej, granitu, chodników, podjazdów. Sprawdź naszą ofertę!'
    return render_template('/uslugi/dla-domu/czyszczenie-kostki-brukowej.html', title='Czyszczenie kostki brukowej', meta_desc=meta_desc, canonical=canonical)


@app.route("/uslugi/dla-domu/czyszczenie-konserwacja-podlog")
def dom_podlogi():
    canonical = url_for('firma_podlogi', _external=True)
    meta_desc = 'Na terenie Bydgoszczy i okolic oferujemy usługi czyszczenia, mycia i impregnacji podłóg, posadzek. Nakładamy powłoki polimerowe. Sprawdź naszą ofertę!'
    return render_template('/uslugi/dla-domu/czyszczenie-podlog.html', title='Czyszczenie i konserwacja podłóg', meta_desc=meta_desc, canonical=canonical)


@app.route("/uslugi/dla-domu/czyszczenie-elewacji-fasad")
def dom_elewacje():
    canonical = url_for('firma_elewacje', _external=True)
    meta_desc = 'Na terenie Bydgoszczy i okolic realizujemy usługi z zakresu czyszczenia i konserwacji elewacji, mycia fasad. Zajrzyj i sprawdź szczegóły naszej oferty!'
    return render_template('/uslugi/dla-domu/czyszczenie-elewacji-fasad.html', title='Czyszczenie elewacji i fasad', meta_desc=meta_desc, canonical=canonical)


@app.route("/uslugi/dla-domu/mycie-powierzchni-szklanych")
def dom_szklo():
    canonical = url_for('firma_szklo', _external=True)
    meta_desc = 'Na terenie Bydgoszczy i okolic oferujemy usługi z zakresu czyszczenia, mycia wszelkich powierzchni szklanych, paneli fotowoltaicznych. Sprawdź szczegóły naszej oferty!'
    return render_template('/uslugi/dla-domu/mycie-powierzchni-szklanych.html', title='Czyszczenie powierzchni szklanych', meta_desc=meta_desc, canonical=canonical)


@app.route("/uslugi/dla-domu/pranie-dywanow-wykladzin")
def dom_dywany():
    canonical = url_for('firma_dywany', _external=True)
    meta_desc = 'Od szeregu lat na terenie Bydgoszczy i okolic realizujemy usługi z zakresu prania dywanów, czyszczenia wykładzin. Popraw estetykę swoich podłóg i sprawdź nas w działaniu!'
    return render_template('/uslugi/dla-domu/pranie-dywanow-wykladzin.html', title='Pranie dywanów i wykładzin', meta_desc=meta_desc, canonical=canonical)


@app.route("/uslugi/dla-domu/czyszczenie-tapicerki-meblowej")
def dom_meble():
    canonical = url_for('firma_meble', _external=True)
    meta_desc = 'Na terenie Bydgoszczy i okolic realizujemy usługi z zakresu prania, czyszczenia tapicerki meblowej. Usuwamy uporczywe plamy z mebli, impregnujemy. Sprawdź naszą ofertę!'
    return render_template('/uslugi/dla-domu/czyszczenie-tapicerki-meblowej.html', title='Czyszczenie mebli i tapicerki', meta_desc=meta_desc, canonical=canonical)


@app.route("/uslugi/dla-domu/czyszczenie-tapicerki-skorzanej")
def dom_meble_skorzane():
    canonical = url_for('firma_meble_skorzane', _external=True)
    meta_desc = 'Na terenie Bydgoszczy i okolic realizujemy usługi czyszczenia i konserwacji tapicerki skórzanej. Wykonujemy okresową pielęgnację mebli skórzanych. Sprawdź naszą ofertę!'
    return render_template('/uslugi/dla-domu/czyszczenie-tapicerki-skorzanej.html', title='Czyszczenie mebli skórzanych', meta_desc=meta_desc, canonical=canonical)


@app.route("/uslugi/dla-domu/ozonowanie-pomieszczen")
def dom_odory():
    canonical = url_for('firma_odory', _external=True)
    meta_desc = 'Na terenie Bydgoszczy i okolic realizujemy usługi z zakresu usuwania odorów, neutralizacji brzydkich zapachów. Oferujemy ozonowanie pomieszczeń. Sprawdź naszą ofertę!'
    return render_template('/uslugi/dla-domu/neutralizacja-odorow.html', title='Ozonowanie pomieszczeń', meta_desc=meta_desc, canonical=canonical)


@app.route("/uslugi/dla-firm")
def uslugi_firma():
    meta_desc = 'Zapraszamy do zapoznania się z naszą ofertą dla Firm. Gwarantujemy szybkie terminy realizacji oraz profesjonalne doradztwo w zakresie czyszczenia i konserwacji powierzchni.'
    return render_template('/uslugi/uslugi-dla-firm.html', title='Usługi dla Firm', meta_desc=meta_desc)


@app.route("/uslugi/dla-firm/mycie-konserwacja-dachow")
def firma_dachy():
    meta_desc = 'Na terenie Bydgoszczy i okolic oferujemy usługi z zakresu czyszczenia, konserwacji i malowania dachów. Odnawiamy powłoki malarskie. Sprawdź szczegóły naszej oferty!'
    return render_template('/uslugi/dla-firm/mycie-konserwacja-dachow.html', title='Czyszczenie, koserwacja i malowanie dachów', meta_desc=meta_desc)


@app.route("/uslugi/dla-firm/czyszczenie-kostki-brukowej")
def firma_kostka():
    meta_desc = 'Na terenie Bydgoszczy i okolic oferujemy usługi z zakresu czyszczenia i impregnacji kostki brukowej, granitu, chodników, podjazdów. Sprawdź naszą ofertę!'
    return render_template('/uslugi/dla-firm/czyszczenie-kostki-brukowej.html', title='Czyszczenie kostki brukowej', meta_desc=meta_desc)


@app.route("/uslugi/dla-firm/czyszczenie-konserwacja-podlog")
def firma_podlogi():
    meta_desc = 'Na terenie Bydgoszczy i okolic oferujemy usługi czyszczenia, mycia i impregnacji podłóg, posadzek. Nakładamy powłoki polimerowe. Sprawdź naszą ofertę!'
    return render_template('/uslugi/dla-firm/czyszczenie-podlog.html', title='Czyszczenie i konserwacja podłóg', meta_desc=meta_desc)


@app.route("/uslugi/dla-firm/czyszczenie-konserwacja-gresu")
def firma_gres():
    meta_desc = 'Na terenie Bydgoszczy i okolic oferujemy usługi czyszczenia i konserwacji posadzek gresowych. Stosujemy skuteczną impregnację. Sprawdź naszą ofertę!'
    return render_template('/uslugi/dla-firm/czyszczenie-konserwacja-gresu.html', title='Czyszczenie i konserwacja gresu', meta_desc=meta_desc)


@app.route("/uslugi/dla-firm/czyszczenie-elewacji-fasad")
def firma_elewacje():
    meta_desc = 'Na terenie Bydgoszczy i okolic realizujemy usługi z zakresu czyszczenia i konserwacji elewacji, mycia fasad. Zajrzyj i sprawdź szczegóły naszej oferty!'
    return render_template('/uslugi/dla-firm/czyszczenie-elewacji-fasad.html', title='Czyszczenie elewacji i fasad', meta_desc=meta_desc)


@app.route("/uslugi/dla-firm/mycie-powierzchni-szklanych")
def firma_szklo():
    meta_desc = 'Na terenie Bydgoszczy i okolic oferujemy usługi z zakresu czyszczenia, mycia wszelkich powierzchni szklanych, paneli fotowoltaicznych. Sprawdź szczegóły naszej oferty!'
    return render_template('/uslugi/dla-firm/mycie-powierzchni-szklanych.html', title='Czyszczenie powierzchni szklanych', meta_desc=meta_desc)


@app.route("/uslugi/dla-firm/pranie-dywanow-wykladzin")
def firma_dywany():
    meta_desc = 'Od szeregu lat na terenie Bydgoszczy i okolic realizujemy usługi z zakresu prania dywanów, czyszczenia wykładzin. Popraw estetykę swoich podłóg i sprawdź nas w działaniu!'
    return render_template('/uslugi/dla-firm/pranie-dywanow-wykladzin.html', title='Pranie dywanów i wykładzin', meta_desc=meta_desc)


@app.route("/uslugi/dla-firm/czyszczenie-tapicerki-meblowej")
def firma_meble():
    meta_desc = 'Na terenie Bydgoszczy i okolic realizujemy usługi z zakresu prania, czyszczenia tapicerki meblowej. Usuwamy uporczywe plamy z mebli, impregnujemy. Sprawdź naszą ofertę!'
    return render_template('/uslugi/dla-firm/czyszczenie-tapicerki-meblowej.html', title='Czyszczenie mebli i tapicerki', meta_desc=meta_desc)


@app.route("/uslugi/dla-firm/czyszczenie-tapicerki-skorzanej")
def firma_meble_skorzane():
    meta_desc = 'Na terenie Bydgoszczy i okolic realizujemy usługi czyszczenia i konserwacji tapicerki skórzanej. Wykonujemy okresową pielęgnację mebli skórzanych. Sprawdź naszą ofertę!'
    return render_template('/uslugi/dla-firm/czyszczenie-tapicerki-skorzanej.html', title='Czyszczenie mebli skórzanych', meta_desc=meta_desc)


@app.route("/uslugi/dla-firm/ozonowanie")
def firma_odory():
    meta_desc = 'Na terenie Bydgoszczy i okolic realizujemy usługi z zakresu usuwania odorów, neutralizacji brzydkich zapachów. Oferujemy ozonowanie pomieszczeń. Sprawdź naszą ofertę!'
    return render_template('/uslugi/dla-firm/neutralizacja-odorow.html', title='Ozonowanie', meta_desc=meta_desc)


@app.route("/uslugi/dla-firm/czyszczenie-hal-magazynow")
def firma_hale():
    meta_desc = 'Posiadamy wieloletnie doświadczenie w zakresie czyszczenia powierzchni elewacji, ścian, dachów, posadzek hal magazynowych i produkcyjnych. Sprawdź naszą ofertę dla Firm!'
    return render_template('/uslugi/dla-firm/czyszczenie-hal-magazynow.html', title='Czyszczenie hal i magazynów', meta_desc=meta_desc)


@app.route("/galeria")
def galeria():
    meta_desc = 'Czyszczenie kostki brukowej, dachów, mycie elewacji, pranie wykładzin, mebli, dywanów... Odwiedź naszą galerię zdjęć z realizacji i zobacz jak działamy!'
    return render_template('galeria.html', title='Galeria', meta_desc=meta_desc)


def get_img_list(path):
    list = [img for img in os.listdir(f'./kwazar_website{ path }') if os.path.isfile(os.path.join(f'./kwazar_website{ path }', img))]
    list.sort()
    return list


@app.route("/galeria/kostka-brukowa")
def galeria_kostka_brukowa():
    meta_desc = 'Wejdź i zobacz nasze zdjęcia z realizacji czyszczenia kostki brukowej, chodników, podjazdów...'
    context = {
        'header': 'Czyszczenie kostki brukowej',
        'path': '/static/img/galeria/kostka-brukowa/',
        'gallery': True
    }

    return render_template('/galeria-zdjecia.html', title=f'{ context["header"] } - Galeria', **context, img_list=get_img_list(context["path"]), meta_desc=meta_desc)


@app.route("/galeria/dachy-elewacje")
def galeria_dachy_elewacje():
    meta_desc = 'Wejdź i zobacz nasze zdjęcia z realizacji czyszczenia i impregnacji dachów, fasad, elewacji...'
    context = {
        'header': 'Mycie dachów, fasad i elewacji',
        'path': '/static/img/galeria/dachy-elewacje/',
        'gallery': True
    }

    return render_template('/galeria-zdjecia.html', title=f'{ context["header"] } - Galeria', **context, img_list=get_img_list(context["path"]), meta_desc=meta_desc)


@app.route("/galeria/podlogi-posadzki")
def galeria_podlogi_posadzki():
    meta_desc = 'Wejdź i zobacz nasze zdjęcia z realizacji czyszczenia i impregnacji podłóg, posadzek...'
    context = {
        'header': 'Czyszczenie podłóg i posadzek',
        'path': '/static/img/galeria/podlogi-posadzki/',
        'gallery': True
    }

    return render_template('/galeria-zdjecia.html', title=f'{ context["header"] } - Galeria', **context, img_list=get_img_list(context["path"]), meta_desc=meta_desc)


@app.route("/galeria/powierzchnie-szklane")
def galeria_powierzchnie_szklane():
    meta_desc = 'Wejdź i zobacz nasze zdjęcia z realizacji czyszczenia powierzchni szklanych, paneli fotowoltaicznych...'
    context = {
        'header': 'Czyszczenie powierzchni szklanych',
        'path': '/static/img/galeria/powierzchnie-szklane/',
        'gallery': True
    }

    return render_template('/galeria-zdjecia.html', title=f'{ context["header"] } - Galeria', **context, img_list=get_img_list(context["path"]), meta_desc=meta_desc)


@app.route("/galeria/referencje-certyfikaty")
def galeria_referencje_certyfikaty():
    meta_desc = 'Posiadamy wieloletnie, udokumentowane doświadczenie w zakresie usług utrzymania czystości. Zobacz nasze referencje i certyfikaty!'
    context = {
        'header': 'Referencje i certyfikaty',
        'path': '/static/img/galeria/referencje-certyfikaty/',
        'gallery': True
    }

    return render_template('/galeria-zdjecia.html', title=f'{ context["header"] } - Galeria', **context, img_list=get_img_list(context["path"]), meta_desc=meta_desc)


@app.route("/galeria/inne")
def galeria_inne():
    meta_desc = 'Wejdź i zobacz nasze zdjęcia z realizacji usług czyszczenia'
    context = {
        'header': 'Czyszczenie innych powierzchni',
        'path': '/static/img/galeria/inne/',
        'gallery': True
    }

    return render_template('/galeria-zdjecia.html', title=f'{ context["header"] } - Galeria', **context, img_list=get_img_list(context["path"]), meta_desc=meta_desc)


@app.route("/cennik")
def cennik():
    meta_desc = 'Zajrzyj i dowiedz się ile kosztuje pranie, odplamianie wykładzin, dywanów, kanapy, sofy, fotela i innych mebli tapicerowanych. Sprawdź szczegóły naszej szerokiej oferty usług!'
    return render_template('cennik.html', title='Cennik', meta_desc=meta_desc,)


def send_contact_email(form):
    msg = Message(f'{ form.title.data } (Formularz kontaktowy z czyszczenie.bydgoszcz.pl)',
                  sender='sender@example.com',
                  reply_to=form.email.data,
                  recipients=['receiver@example.com'])
    msg.body = f'Nadawca: { form.email.data }\nTreść wiadomości:\n{ form.content.data }'
    if form.picture.data:
        msg.attach(
            form.picture.data.filename,
            'image/*',
            form.picture.data.read())
    mail.send(msg)


@app.route("/kontakt", methods=['GET', 'POST'])
def kontakt():
    meta_desc = 'Kontakt do firmy czyszczącej - napisz lub zadzwoń do nas! Posiadamy szeroką ofertę usług czyszczenia, mycia i impregnacji na terenie Bydgoszczy i okolic.'
    form = ContactForm()
    if request.method == "POST":
        if form.validate() == False:
            flash('Formularz zawiera błędy', 'danger')
        else:
            send_contact_email(form)
            flash('Wiadomość została wysłana. Wkrótce się z Tobą skontaktujemy!', 'info')
            return redirect(url_for('kontakt'))
    return render_template('kontakt.html', title='Kontakt', form=form, meta_desc=meta_desc, kontakt=True)


@app.route("/cookies")
def cookies():
    return render_template('cookies.html', title='Polityka plików cookies', noindex=True)


@app.route("/panel", methods=['GET', 'POST'])
def panel():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('lista'))
    if form.validate_on_submit():
        user = User.query.filter_by(login=form.login.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('lista'))
        else:
            flash(f'Podano niepoprawne dane', 'danger alert-dismissible fade show')
    return render_template('panel.html', title='Logowanie', form=form)


@app.route("/panel/lista")
@login_required
def lista():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=6)
    return render_template('/panel/lista.html', title='Panel', posts=posts)


@app.route("/panel/dodaj-post", methods=['GET', 'POST'])
@login_required
def dodaj_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data)
        db.session.add(post)
        db.session.commit()
        flash(f'Post "{post.title}" został dodany!', 'success')
        return redirect(url_for('lista'))
    return render_template('/panel/dodaj.html', title='Dodaj post', form=form)


@app.route("/panel/lista/<int:post_id>", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash(f'Post "{post.title}" został zaktualizowany!', 'info alert-dismissible fade show')
        return redirect(url_for('lista'))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('/panel/dodaj.html', title='Edytuj post', form=form)


@app.route("/panel/lista/<int:post_id>/usun", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash(f'Post "{post.title}" został usunięty!', 'danger alert-dismissible fade show')
    return redirect(url_for('lista'))


@app.route("/panel/wyloguj")
@login_required
def logout():
    logout_user()
    flash(f'Pomyślnie wylogowano', 'info')
    return redirect(url_for('panel'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title='Nie znaleziono', noindex=True), 404
