from enum import Enum


class InteractionType(Enum):
    post_daily_to_friends = "post daily to my friends"
    post_daily_for_work = "post daily for work"
    post_rarely_for_friends = 'post rarely for my friends'
    post_rarely_for_work = 'post rarely for work'
    never_post = 'never post'


class PerpetratorType(Enum):
    person_you_know = "person you know"
    multiple_person_you_know = "multiple persons you know"
    single_stranger = "single stranger"
    multiple_stranger = 'multiple strangers'


class ReactionType(Enum):
    my_behaviour_has_not_changed = "my behaviour has not changed"
    i_avoid_controversial_topics = "i avoid controversial topics and self-censor"
    i_took_a_break_from_platform = "i took a break from platform"
    no_longer_post_pictures = "i no longer post pictures of myself"
    no_longer_use_platform = "i no longer use platform"
