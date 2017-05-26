from flask import render_template, Flask
from flask_wtf import Form
from wtforms import RadioField, StringField
import meetup.api
from flask_wtf.csrf import CSRFProtect
app = Flask(__name__)
app.secret_key = '391719'

csrf = CSRFProtect(app)

MEETUP_API_KEY = '55371e32684412531e506216216b2e'

def get_names():
    client = meetup.api.Client(MEETUP_API_KEY)
    rsvps=client.GetRsvps(event_id='237109845', urlname='_ChiPy_')
    member_id = ','.join([str(i['member']['member_id']) for i in rsvps.results])
    members = client.GetMembers(member_id=member_id)
    return members.results

class AttendeeForm(Form):
    project_type = RadioField(choices=[('Solo', 'Solo'), ('Team', 'Team')])
    lines_of_code = StringField()

@app.route('/')
def attendee_page():
    members = get_names()
    form = AttendeeForm()
    return render_template('attendee.html', members=members, form=form)

if __name__ == '__main__':
    app.run(debug=True)
