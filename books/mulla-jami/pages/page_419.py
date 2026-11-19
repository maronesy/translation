# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 419 (printed ٤١٨)."""

PAGE_NUMBER = 419
PRINTED_PAGE = "٤١٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Follows «أي: هذا باب بيان المعرفة والنكرة من أقسام الاسم.» at the foot of PDF p. 418 (new sentence).
    {"type": "matn",
     "ar": "(المعرفة: ما) أي: اسم (وضع) بوضع جزئي[[١]] أو كلي (لشيء) متلبس (بعينه) أي: بذاته المتعينة[[٢]] المعلومة للمتكلم والمخاطب[[٣]] المعهودة بينهما،",
     "en": "(The definite is what), that is, a noun that (has been coined), by particular or universal coinage, (for a thing) taken (in its specificity), that is, in its determinate essence, known to the speaker and the addressee and familiar between them."},
    {"type": "matn",
     "ar": "فالشيء مقيدا بهذه المعلومية والمعهودية إذا وضع له اسم فهو المعرفة،",
     "en": "So when a noun is coined for a thing restricted by this being known and familiar, it is the definite;"},
    {"type": "matn",
     "ar": "وإذا وضع له اسم باعتبار ذاته مع قطع النظر عن هذه الحيثية فهو النكرة.",
     "en": "and when a noun is coined for it with regard to its essence, disregarding this respect, it is the indefinite."},
    {"type": "matn",
     "ar": "فقوله: «ما وضع لشيء» شامل للمعرفة والنكرة.",
     "en": "His words “what has been coined for a thing” cover both the definite and the indefinite."},
    {"type": "matn",
     "ar": "وقوله: «بعينه» يخرج به النكرة[[٤]].",
     "en": "His words “in its specificity” exclude the indefinite."},
    {"type": "matn",
     "ar": "(وهي) أي: المعرفة ستة أنواع بالاستقراء، وأشار[[٥]] بترتيبها في الذكر إلى ترتيبها[[٦]]",
     "en": "(And it), that is, the definite, is of six kinds by induction; by their order in mention he indicated their order…"},

    {"type": "rule"},

    # ---------------- Footnote continued from PDF p. 418 (footnote ٧) ----------------
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "كما في المشتقات، فإن اسم الفاعل مثلا موضوع لمن قام الفعل به،",
     "en": "…as in derived nouns: the active participle, for example, is coined for whoever the action subsists in;"},
    {"type": "pair",
     "ar": "أو يلاحظ الموضوع له بوجه أعم كما في الحروف والمضمرات والمبهمات،",
     "en": "or what it is coined for is considered in a more general respect, as in particles, pronouns and demonstratives (mubhamāt)."},
    {"type": "pair",
     "ar": "فههنا أربعة احتمالات أن يكون كلاهما ملحوظين بخصوصهما، أو كلاهما بعمومهما، أو الموضوع يكون ملحوظا بخصوصه، والموضوع له بعمومه أو بالعكس، ولا وجود للاحتمال الثاني.",
     "en": "Here there are four possibilities: that both are considered in their particularity; or both in their generality; or that the coined expression is considered in its particularity and what it is coined for in its generality; or the reverse. The second possibility does not occur."},
    # REVIEW: «ولا وجود للاحتمال الثاني» printed so; on the enumeration as printed the non-occurring case would normally be the third; transcribed as printed.

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "الوضع الجزئي ما لوحظ فيه الموضوع له الجزئي بعينه ويسمى وضعا خاصا أيضا،",
     "en": "Particular coinage is that in which the particular thing coined for is considered in itself; it is also called specific coinage (waḍʿ khāṣṣ)."},
    {"type": "pair",
     "ar": "والوضع الكلي ما لوحظ فيه الموضوع له الكلي بنفسه، أو الموضوع له بعنوان أعم",
     "en": "Universal coinage is that in which the universal thing coined for is considered in itself, or the thing coined for is considered under a more general heading,"},
    {"type": "pair",
     "ar": "كما يقال: لوحظ كل مشار إليه بعنوان المشار إليه، ووضع له بعينه اسم الإشارة، ويسمى وضعا عاما أيضا،",
     "en": "as when it is said: every thing pointed to is considered under the heading “what is pointed to”, and the demonstrative is coined for it in its specificity; this is also called general coinage (waḍʿ ʿāmm)."},
    {"type": "pair",
     "ar": "فالأول: وضع عام لموضوع له عام، والثاني: وضع عام لموضوع له خاص.",
     "en": "The first is general coinage for a general thing coined for, and the second is general coinage for a specific thing coined for."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "فالعين بمعنى الذات كما في القاموس وغيره، وإضافته إلى الضمير للعهد، فيصير بمعنى ذاته المتعينة المعلومة المعهودة،",
     "en": "So “ʿayn” means essence, as in al-Qāmūs and elsewhere, and its annexation to the pronoun is for prior reference, so that it comes to mean its determinate, known, familiar essence."},
    {"type": "pair",
     "ar": "والعهد إنما يعتبر بين المتكلم والمخاطب لا غيرهما، ولا بد في المعرفة من علم المتكلم؛ إذ لا يمكن إعلام المعهود بدون العلم به.",
     "en": "Familiarity is considered only between the speaker and the addressee, not others; and in the definite the speaker’s knowledge is indispensable, since one cannot make known what is familiar without knowing it."},
    {"type": "pair",
     "ar": "في الإقليد: التعريف يتعلق إما بمعرفة المتكلم دون المخاطب نحو قولك: «لي بستان» وأنت تعرفه دون مخاطبك،",
     "en": "In al-Iqlīd: definiteness relates either to what the speaker knows and the addressee does not, as in your saying “lī bustānun” (I have a garden) when you know it and your addressee does not;"},
    {"type": "pair",
     "ar": "أو بما لا يعرفانه نحو قولك: أنا في طلب غلام اشتد به، ولست تقصد به إلى معين،",
     "en": "or to what neither of them knows, as in your saying “I am looking for a boy to rely on”, when you do not mean anyone specific by it;"},
    {"type": "pair",
     "ar": "وبما يعرفانه نحو قولك: فعل الرجل كذا.",
     "en": "or to what both of them know, as in your saying “the man did such and such”."},
    {"type": "pair",
     "ar": "وما قيل: إن المعرفة ما يعرفه مخاطبك فمعناه أنه لا بد فيها من معرفة المخاطب.",
     "en": "As for what has been said—that the definite is what your addressee knows—its meaning is that the addressee’s knowledge is indispensable in it."},
    {"type": "pair",
     "ar": "وإنما زاد المعينة إشارة إلى أن ما وقع في عباراتهم في لفظة المعينة معناه المعلومة المشخصة.",
     "en": "He added “determinate” only to indicate that the word “determinate”, where it occurs in their expressions, means known and individuated."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لا اعتداد بعلم المتكلم في التعريف ولذلك يقال: حقيقة التعريف الإشارة إلى ما يعرفه المخاطب.",
     "en": "The speaker’s knowledge is not taken into account in definiteness; for this reason it is said: the reality of definiteness is pointing to what the addressee knows."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "يبقى بعد النكرة التي كان علما نكرت بالتأويل، وهو مما جعله الرضي عين هذا التعريف، فعدل عنه إلى ما لا يحتمل المقام بيانه،",
     "en": "There remains, after this, the indefinite that was a proper name and was made indefinite by interpretation; this is among the things al-Raḍī made the very [objection to] this definition, so he turned from it to something whose explanation this place cannot bear."},
    {"type": "pair",
     "ar": "ولا يبعد أن يقال: إطلاق النكرة عليه تجوز لما أنه في حكم النكرة، ويعامل به معاملتها.",
     "en": "It is not far-fetched to say: calling it indefinite is figurative, because it has the status of the indefinite and is treated as it is treated."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "وذلك بليغ، فلا بد لاختياره هذا الترتيب المذكور من نكتة.",
     "en": "This is eloquent; so there must be a subtle reason (nukta) for his choosing this order of mention."},
    {"type": "pair",
     "ar": "والإشارة إلى ترتيبها في المرتبة تصلح نكتة لذلك، فلتحمل عليه.",
     "en": "Indicating their order in rank is fit to be a subtle reason for it, so let it be taken in that sense."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "في المرتبة على ما اختاره. وتبع الزمخشري في ذلك،",
     "en": "[That is,] in rank, according to what he chose. In this he followed al-Zamakhsharī,"},
    {"type": "pair",
     "ar": "فإنه ذكرها في المفصل على هذا الترتيب إلا في المضاف حيث جعل تعريفه بعد جميع الأنواع، كما هو مذهب المبرد؛ لأن تعريفه في غيره.",
     "en": "for he listed them in al-Mufaṣṣal in this order, except for the annexed noun, whose definiteness he placed after all the kinds, as is the doctrine of al-Mubarrad, because its definiteness lies in another."},
    {"type": "pair",
     "ar": "والزمخشري جعله في مرتبة المضاف، كما هو مذهب سيبويه.",
     "en": "Al-Zamakhsharī placed it in the rank of [the term] it is annexed to, as is the doctrine of Sībawayh."},
]
