from pyramid.events import (
    subscriber,
    ApplicationCreated,
    NewRequest,
    ContextFound,
    NewResponse,
    BeforeRender,
)


@subscriber(ApplicationCreated)
def application_created(event):
    print("~~~ new application created: {}".format(event))


@subscriber(NewRequest)
def new_request_created(event):
    print("~~~ new request created: {}".format(event))


@subscriber(ContextFound)
def context_found(event):
    print("~~~ context found: {}".format(event))


@subscriber(BeforeRender)
def before_render(event):
    print("~~~ before rendering: {}".format(event))


@subscriber(NewResponse)
def new_response_created(event):
    print("~~~ new response created: {}".format(event))
