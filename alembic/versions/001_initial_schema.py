"""initial schema

Revision ID: 001_initial
Revises:
Create Date: 2026-04-16

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "001_initial"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("email", sa.String(length=100), nullable=False),
        sa.Column("password", sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    op.create_table(
        "theater",
        sa.Column("theater_id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("theater_name", sa.String(length=100), nullable=False),
        sa.Column("theater_location", sa.String(length=200), nullable=False),
        sa.Column("total_capacity", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("theater_id"),
    )
    op.create_table(
        "movie",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("movie_name", sa.String(length=100), nullable=False),
        sa.Column("movie_type", sa.String(length=100), nullable=False),
        sa.Column("duration", sa.Integer(), nullable=False),
        sa.Column("movie_language", sa.String(length=100), nullable=False),
        sa.Column("cast_summary", sa.String(length=500), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "seat",
        sa.Column("seat_id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("seat_row", sa.String(length=10), nullable=False),
        sa.Column("seat_col", sa.Integer(), nullable=False),
        sa.Column("seat_type", sa.String(length=50), nullable=False),
        sa.Column("theater_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["theater_id"],
            ["theater.theater_id"],
        ),
        sa.PrimaryKeyConstraint("seat_id"),
    )
    op.create_table(
        "schedules",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("movie_id", sa.Integer(), nullable=False),
        sa.Column("theater_id", sa.Integer(), nullable=False),
        sa.Column("show_datetime", sa.DateTime(), nullable=False),
        sa.Column("ticket_price", sa.Float(), nullable=False),
        sa.ForeignKeyConstraint(
            ["movie_id"],
            ["movie.id"],
        ),
        sa.ForeignKeyConstraint(
            ["theater_id"],
            ["theater.theater_id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "ticket",
        sa.Column("ticket_id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("schedule_id", sa.Integer(), nullable=False),
        sa.Column("seat_id", sa.Integer(), nullable=False),
        sa.Column("booking_time", sa.DateTime(), nullable=False),
        sa.Column("payment_status", sa.String(length=50), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.ForeignKeyConstraint(
            ["schedule_id"],
            ["schedules.id"],
        ),
        sa.ForeignKeyConstraint(
            ["seat_id"],
            ["seat.seat_id"],
        ),
        sa.PrimaryKeyConstraint("ticket_id"),
        sa.UniqueConstraint("schedule_id", "seat_id", name="uq_ticket_schedule_seat"),
    )


def downgrade() -> None:
    op.drop_table("ticket")
    op.drop_table("schedules")
    op.drop_table("seat")
    op.drop_table("movie")
    op.drop_table("theater")
    op.drop_table("users")
