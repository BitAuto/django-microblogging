from django.db.models import get_models, signals
from django.utils.translation import ugettext_noop as _

try:
    from notification.models import NotificationType
    
    def create_notice_types(app, created_models, verbosity, **kwargs):
        NotificationType.create("tweet_follow", _("New Tweet Follower"), _("someone has started following your tweets"))
        NotificationType.create("tweet_reply_received", _("New Tweet Reply"), _("someone sent a tweet reply to you"))
    
    signals.post_syncdb.connect(create_notice_types, sender=notification)
except ImportError:
    print "Skipping creation of NoticeTypes as notification app not found"
