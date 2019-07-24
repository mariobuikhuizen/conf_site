from django.db.models import Q
from django.http import Http404
from django.views.generic import ListView

from symposion.speakers.models import Speaker

from conf_site.core.views import CsvView, SlugDetailView, SlugRedirectView


class SpeakerDetailView(SlugDetailView):
    context_object_name = "speaker"
    model = Speaker
    template_name = "symposion/speakers/speaker_profile.html"
    view_name = "speaker_profile"

    def _get_presentations(self):
        """Utility method to retrive a speaker's presentations."""
        speaker = self.get_object()
        return list(speaker.presentations.exclude(slot=None)) + list(
            speaker.copresentations.exclude(slot=None)
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Add speaker's presentations to context.
        # This is necessary because we need
        # a speaker's "copresentations" as well.
        presentations = self._get_presentations()
        context["presentations"] = presentations

        return context

    def render_to_response(self, context, **response_kwargs):
        # Verify that speaker has presentations (or user is staff).
        presentations = self._get_presentations()
        if not presentations and not self.request.user.is_staff:
            raise Http404()

        return super().render_to_response(context, **response_kwargs)


class SpeakerRedirectView(SlugRedirectView):
    model = Speaker
    redirect_view_name = "speaker_profile"


class SpeakerListView(ListView):
    """Show all speakers with presentations."""

    context_object_name = "speakers"
    queryset = (
        Speaker.objects.filter(
            Q(presentations__gt=0) | Q(copresentations__gt=0)
        )
        .order_by()
        .distinct()
    )
    template_name = "speakers/speaker_list.html"


class ExportAcceptedSpeakerEmailView(CsvView):
    """Export email addresses of speakers with accepted presentations."""
    csv_filename = "accepted-speaker-emails.csv"

    def get(self, *args, **kwargs):
        self.csv_writer.writerow(["Name", "Email Address"])

        # Iterate through speakers.
        # Add speakers with accepted presentations to temp file.
        for speaker in Speaker.objects.all():
            if speaker.all_presentations:
                self.csv_writer.writerow([speaker.name, speaker.email])

        return super(ExportAcceptedSpeakerEmailView, self).get(*args, **kwargs)
