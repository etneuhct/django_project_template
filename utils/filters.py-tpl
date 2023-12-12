from rest_framework import filters


class ExclusionFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        prefix = "excluded"
        exclusion_fields = getattr(view, 'exclusion_fields', [])
        for field in exclusion_fields:
            exclude_values = request.query_params.getlist(f'{prefix}__{field}')
            if exclude_values:
                filter_kwargs = {f"{field}__in": exclude_values}
                queryset = queryset.exclude(**filter_kwargs)

        return queryset
