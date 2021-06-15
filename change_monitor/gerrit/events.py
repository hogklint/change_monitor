import json
from abc import ABC, abstractmethod
from gerrit import structures


class Event(ABC):
    def __init__(self, json_data):
        self.json_data = json_data

    # @abstractmethod
    def to_string(self):
        return json.dumps(self.json_data)

    @property
    def id(self):
        if "change" in self.json_data and "id" in self.json_data["change"]:
            return self.json_data["change"]["id"]
        else:
            return None


class AssigneeChanged(Event):
    pass


class ChangeAbandoned(Event):
    pass


class ChangeDeleted(Event):
    pass


class ChangeMerged(Event):
    pass


class ChangeRestored(Event):
    pass


class CommentAdded(Event):
    pass


class DroppedOutput(Event):
    pass


class HashtagsChanged(Event):
    pass


class ProjectCreated(Event):
    pass


class PatchsetCreated(Event):
    pass


class RefReplicated(Event):
    pass


class RefReplicationDone(Event):
    pass


class RefReplicationScheduled(Event):
    pass


# TODO: Ignore for now, has no associated change
class RefUpdated(Event):
    @property
    def id(self):
        return None


class ReviewerAdded(Event):
    pass


class ReviewerDeleted(Event):
    pass


class TopicChanged(Event):
    pass


class VoteDeleted(Event):
    pass


class WipStateChanged(Event):
    pass


class PrivateStateChanged(Event):
    pass


def create_event(line):
    json_data = json.loads(line)
    event_type = json_data["type"]
    if event_type in _events_map:
        return _events_map[event_type](json_data)


_events_map = {
    "assignee-changed": AssigneeChanged,
    "change-abandoned": ChangeAbandoned,
    "change-deleted": ChangeDeleted,
    "change-merged": ChangeMerged,
    "change-restored": ChangeRestored,
    "comment-added": CommentAdded,
    "dropped-output": DroppedOutput,
    "hashtags-changed": HashtagsChanged,
    "project-created": ProjectCreated,
    "patchset-created": PatchsetCreated,
    # "ref-updated": RefUpdated,
    "reviewer-added": ReviewerAdded,
    "reviewer-deleted": ReviewerDeleted,
    "topic-changed": TopicChanged,
    "vote-deleted": VoteDeleted,
    "wip-state-changed": WipStateChanged,
    "private-state-changed": PrivateStateChanged,
}
