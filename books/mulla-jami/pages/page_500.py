# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 500 (printed ٤٩٩)."""

PAGE_NUMBER = 500
PRINTED_PAGE = "٤٩٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # PDF p. 499 ends with the list of the particles of conditionality «(وما، ومن، وأي، وأنى).»; a new sentence begins here.
    {"type": "matn",
     "ar": "(وأما) انجزام المضارع (مع «كيفما» و«إذا» فشاذ) لم يجيء[[١]] في كلامهم على وجه الاطراد.",
     "en": "(As for) the muḍāriʿ’s being put in the jussive (with “kayfamā” and “idhā”, it is anomalous (shādhdh)): it has not occurred in their speech as a regular pattern."},
    {"type": "matn",
     "ar": "أما مع «كيفما»: فلأن معناه عموم الأحوال،",
     "en": "As for [its occurring] with “kayfamā”: that is because its meaning is the generality of states;"},
    {"type": "matn",
     "ar": "فإذا قلت:« كيفما تقرأ أقرأ» كان معناه: «على أي حال وكيفية تقرأ أنت أنا أيضا أقرأ عليها»،",
     "en": "so if you say “kayfamā taqraʾ aqraʾ” (however you recite, I recite), its meaning is: “in whatever state and manner you recite, I too recite in it”;"},
    {"type": "matn",
     "ar": "ومن المتعذر[[٢]] استواء قراءة قارئين في جميع الأحوال والكيفيات.",
     "en": "and it is impossible for the recitation of two reciters to be equal in all states and manners."},
    {"type": "matn",
     "ar": "وأما مع «إذا» فلأن كلمات الشرط إنما تجزم لتضمنها مع «إن» التي هي موضوعة للإبهام، و«إذا» موضوعة للأمر المقطوع به.",
     "en": "As for [its occurring] with “idhā”: that is because the words of condition put [the verb] in the jussive only because they implicitly contain [the sense of] “in”, which is coined for indeterminacy, whereas “idhā” is coined for what is certain."},
    {"type": "matn",
     "ar": "(وب«إن» مقدرة) عطف على قوله ب«لم» أي: وينجزم المضارع ب«إن» مقدرة، وسيجيء بيانه إن شاء الله تعالى.",
     "en": "(And by “in” when supposed [but unexpressed]): coordinated with his words “by lam”, that is: the muḍāriʿ is put in the jussive by a supposed “in”. Its explanation will come, if Allah the Exalted wills."},
    {"type": "matn",
     "ar": "(ف«لم» لقلب المضارع ماضيا ونفيه) أي: نفي المضارع،",
     "en": "(So “lam” is for turning the muḍāriʿ into a past and negating it), that is, negating the muḍāriʿ;"},
    {"type": "matn",
     "ar": "ولا يبعد[[٣]] لو جعل الضمير عائدا إلى ما هو أقرب أعني: ماضيا.",
     "en": "and it would not be far-fetched if the pronoun were made to refer to what is nearer, I mean “a past”."},
    {"type": "matn",
     "ar": "(و«لما» مثلها) أي: مثل «لم» في هذا القلب والنفي.",
     "en": "(And “lammā” is like it), that is, like “lam”, in this turning [into the past] and negation."},
    {"type": "matn",
     "ar": "(وتختص) أي: «لما» (بالاستغراق[[٤]]) أي: استغراق أزمنة الماضي من وقت الانتفاء إلى وقت التكلم ب«لما».",
     "en": "(And it is distinguished), that is, “lammā”, (by comprehensiveness (istighrāq)), that is, by comprehending the times of the past from the moment the negation began up to the moment of speaking with “lammā”."},
    {"type": "matn",
     "ar": "تقول: «ندم فلان ولم ينفعه الندم» أي: عقيب ندمه، ولا يلزم استمرار انتفاء انتفاع الندم إلى وقت التكلم بها،",
     "en": "You say “nadima fulānun wa-lam yanfaʿhu al-nadamu” (so-and-so repented, and the repentance did not benefit him), that is, right after his repenting; and it does not follow that the absence of benefit from the repentance continues up to the moment of speaking with it;"},
    {"type": "matn",
     "ar": "وإذا قلت: «ندم فلان ولما ينفعه الندم» أفاد استمرار ذلك إلى وقت التكلم بها.",
     "en": "but if you say “nadima fulānun wa-lammā yanfaʿhu al-nadamu” (so-and-so repented, and the repentance has not yet benefited him), it conveys that this continues up to the moment of speaking with it."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: ليس معنى الشاذ مخالف القياس ولا مخالف الاستعمال الفصيح؛",
     "en": "That is, the meaning of “anomalous” here is not “contrary to analogy (qiyās)”, nor “contrary to eloquent usage”;"},
    {"type": "pair",
     "ar": "لأنهما إذا تضمنا معنى الشرط، فانجزام المضارع بعدهما قياسي واقع في استعمال الفصحاء،",
     "en": "for when the two of them contain the sense of condition, the muḍāriʿ’s being put in the jussive after them is analogical and occurs in the usage of the eloquent;"},
    {"type": "pair",
     "ar": "بل معناه أن الجزم بعدهما مع إرادة معنى الشرط قليل لم يسمع في السعة.",
     "en": "rather, its meaning is that the jussive after them, with the sense of condition intended, is rare and has not been heard in free usage (al-saʿa) [as opposed to poetic necessity]."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    # REVIEW: footnote ٢ prints «مضتمنة» (apparently for «متضمنة»); transcribed as printed.
    {"type": "pair",
     "ar": "فإن تعذر الاستواء تعذر اعتبار معنى الشرط فيه، فلا تكون مضتمنة لمعنى «إن» فلا تجزم.",
     "en": "For if the equality is impossible, considering the sense of condition in it is impossible; so it does not contain the sense of “in”, and so it does not put [the verb] in the jussive."},
    {"type": "pair",
     "ar": "وأما ما جاء في الشعر فللضرورة بإجرائه مجرى الشرط لكونه في صورته،",
     "en": "As for what occurs in poetry, it is out of necessity, by treating it as the condition is treated, since it has its form;"},
    {"type": "pair",
     "ar": "أو باعتبار عدم الاعتداد ببعض الأحوال والكيفيات، واعتبار استوائها في البعض،",
     "en": "or by disregarding some of the states and manners and considering their equality in some;"},
    {"type": "pair",
     "ar": "وبذلك ضعفت الشرطية فلم تجزم.",
     "en": "and by that the conditional force is weakened, so it does not put [the verb] in the jussive."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: من حيث المعنى، وفيه إشارة إلى بعده في الجملة.",
     "en": "That is, with respect to meaning; and in it there is an indication that it is somewhat far-fetched on the whole."},
    {"type": "pair",
     "ar": "وذلك لأن لم يدخل على المضارع، ويؤثر في القلب والنفي معا،",
     "en": "That is because lam enters upon the muḍāriʿ and effects both the turning [into the past] and the negation together;"},
    {"type": "pair",
     "ar": "وكونه لنفي الماضي إنما يصح لو اعتبر النفي بعد القلب، وهو خلاف الظاهر، ولذا زاد كلمة «لو»،",
     "en": "and its being for negating the past is valid only if the negation is considered as coming after the turning, which is contrary to the apparent; that is why he added the word “law” (if);"},
    {"type": "pair",
     "ar": "وإلا فالظاهر ولا يبعد لو جعل الضمير إلى آخره،",
     "en": "otherwise the apparent [reference would hold]. “And it would not be far-fetched if the pronoun were made…” to the end:"},
    {"type": "pair",
     "ar": "نعم يصح لو قيل: لقلب الماضي مضارعا، ونفيه على ما ذهب إليه بعضهم من أن «لم» دخل على الماضي، فقلب لفظه إلى لفظ المضارع،",
     "en": "yes, it would be valid if it were said “for turning the past into a muḍāriʿ and negating it”, according to the view some have held that “lam” enters upon the past and turns its wording into the wording of the muḍāriʿ;"},
    # REVIEW: footnote ٣ prints «ولكمة» (apparently for «وكلمة»); transcribed as printed.
    {"type": "pair",
     "ar": "ولكمة «لو» شرطية دل على جوابه ما قبله.",
     "en": "and the word “law” is conditional, its apodosis being indicated by what precedes it."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "ولا يبعد أن يستفاد ذلك من تأكيد لم بما النافية، فيكون تركيب لما من كلمة لم وما.",
     "en": "It is not far-fetched that this be derived from the reinforcing of lam by the negative mā, so that lammā is compounded of the words lam and mā."},
]
