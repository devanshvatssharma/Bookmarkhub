from . import views
from django.urls import path
urlpatterns = [
    path("dashboard/",views.dashboard_view,name="dashboard"),
    path("bookmarks/",views.BookmarkPageView.as_view(),name="bookmarks"),
    path("bookmarks/add",views.AddBookmarkView.as_view(),name="bookmarkadd"),
    path("bookmarks/<int:pk>",views.BookmarkDetailView.as_view(),name="bookmarkdetail"),
    path("bookmarks/<int:pk>/edit",views.BookmarkUpdateView.as_view(),name="bookmarkupdate"),
    path("bookmarks/<int:pk>/delete",views.DeleteBookmarkView.as_view(),name="bookmarkdelete"),
    path("collections/",views.CollectionPageView.as_view(),name="collections"),
    path("collections/add",views.CollectionAddView.as_view(),name="collectionadd"),
    path("collections/<int:pk>/edit",views.CollectionUpdateView.as_view(),name="collectionupdate"),
    path("collections/<int:pk>/delete",views.CollectionDeleteView.as_view(),name="collectiondelete"),
    path("tags/",views.TagPageView.as_view(),name="tags"),
    path("tags/add",views.AddTagView.as_view(),name="tagsadd"),
    path("tags/<int:pk>/edit",views.UpdateTagView.as_view(),name="tagupdate"),
    path("tags/<int:pk>/delete",views.DeleteTagView.as_view(),name="tagdelete"),
    path("profile/",views.ProfileDetailView,name="profile"),
    path("profile/<int:pk>/edit",views.ProfileUpdateView.as_view(),name="profileupdate"),
    path("delete_user/",views.delete_user,name="deleteuser"),
]
