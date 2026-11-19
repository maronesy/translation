# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 424 (printed ٤٢٣)."""

PAGE_NUMBER = 424
PRINTED_PAGE = "٤٢٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «ثم المضمر الغائب، ولم يذكره؛ لأنه علم من أعرفية المتكلم والمخاطب أنه أدون» at the foot of PDF p. 423.
    {"type": "matn",
     "ar": "منهما، واقتصر على بيان النسبة بين أصناف المضمرات، فإن سائر المعارف لا تفاوت بين أصنافها إلا المضاف إلى أحدها،",
     "en": "…than both. He confined himself to stating the relation among the sub-classes of pronouns, for among the sub-classes of the other definite nouns there is no difference in degree, except for what is annexed to one of them,"},
    {"type": "matn",
     "ar": "فإن فيه تفاوتا باعتبار تفاوت المضاف إليه، ولهذا ما أثبت التفاوت بين أصنافه بعد بيانه بين أنواع المضاف إليه وأصنافه،",
     "en": "for in it there is a difference in degree according to the difference of the noun to which it is annexed; this is why he did not establish the difference among its sub-classes after stating it among the kinds of the noun annexed to and their sub-classes."},
    {"type": "matn",
     "ar": "وهذا الترتيب الذي ذكره هو مذهب سيبويه، فإن فيه اختلافات كثيرة.",
     "en": "This ranking that he mentioned is the doctrine of Sībawayh; for there are many disagreements about it."},
    {"type": "matn",
     "ar": "(والنكرة: ما وضع لشيء لا بعينه) أي: لا باعتبار ذاته المتعينة المعلومة المعهودة من حيث هو كذلك.",
     "en": "(The indefinite noun (nakira) is what is imposed for a thing not in its very identity), that is, not with regard to its determinate, known and familiar essence insofar as it is such."},
    {"type": "matn",
     "ar": "فقوله: «ما وضع لشيء» شامل للمعرفة والنكرة.",
     "en": "So his words “what is imposed for a thing” cover both the definite and the indefinite noun."},
    {"type": "matn",
     "ar": "وبقوله: «لا بعينه» خرجت المعرفة.",
     "en": "By his words “not in its very identity” the definite noun is excluded."},

    {"type": "section", "ar": "[أسماء العدد]",
     "en": "The Number Nouns"},

    {"type": "matn",
     "ar": "(أسماء العدد) إنما أفردها بالذكر؛ لأن لها أحكاما خاصة ليست لغيرها،",
     "en": "(The number nouns (asmāʾ al-ʿadad)): he treated them separately only because they have particular rulings that do not belong to others."},
    {"type": "matn",
     "ar": "وهي (ما وضع) أي: ألفاظ وضعت (لكمية آحاد الأشياء) منفردة كانت تلك الآحاد أو مجتمعة[[١]]،",
     "en": "They are (what is imposed), that is, expressions imposed, (for the quantity of the units of things), whether those units are single or combined."},
    {"type": "matn",
     "ar": "فالأشياء هي المعدودات، وآحادها كل واحد واحد منها، وكمية الآحاد ما",
     "en": "The “things” are the things counted; their “units” are each single one of them; and “the quantity of the units” is what…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "إشارة إلى جواب ذكره الهندي عن إشكال الرضي حيث قال: يخرج عنه الواحد والاثنان؛ لأنهما وإن وضعا للكمية، لكن لم يوضعا لكمية الآحاد، بل لكمية الواحد والاثنين.",
     "en": "[This is] an indication of an answer that al-Hindī gave to al-Raḍī’s difficulty, where he said: “one” and “two” are excluded from it, because, although they are imposed for quantity, they are not imposed for the quantity of units but for the quantity of one and of two."},
    {"type": "pair",
     "ar": "ومحصل الجواب: أن واحدا وضع لكمية آحاد الأشياء منفردة لا مجتمعة.",
     "en": "The gist of the answer: “one” is imposed for the quantity of the units of things taken singly, not combined."},
    {"type": "pair",
     "ar": "ونحن نقول: قد حقق الرضي في بحث التعريف باللام أن الجمع المحلى باللام يشمل كل واحد واحد كل اثنين اثنين وكل جماعة جماعة،",
     "en": "We say: al-Raḍī established, in the discussion of definiteness by the lām, that the plural adorned with the lām covers each single one, each two and each group,"},
    {"type": "pair",
     "ar": "فلذا يصح استثناء أيهما شئت عنه فتقول: جاء العلماء إلا واحدا أو اثنين أو جماعة، فإنه في معنى جاءني كل واحد من العلماء، وكل اثنين وكل جماعة،",
     "en": "which is why it is valid to except from it whichever of them you wish, so you say: “the scholars came except one”, or “two”, or “a group”; for it has the meaning of “every one of the scholars came to me, and every two and every group”."},
    {"type": "pair",
     "ar": "والمضاف المستغرق كالمحلى باللام فآحاد الأشياء في معنى كل واحد منها، وكل انثني منها، وكل جماعة منها، فلا إشكال،",
     "en": "The all-inclusive annexed noun is like the one adorned with the lām; so “the units of things” has the meaning of “each one of them, each two of them and each group of them”, and there is no difficulty."},
    # REVIEW: «انثني» is printed with the nūn and thāʾ transposed (for «اثني/اثنين»); transcribed as printed.
    {"type": "pair",
     "ar": "ومما حققه الرضي أن الكمية كلمة نسبية أي الصفة المنسوبة إلى «كم»، وهو العدد المعين الذي يجاب به عن «كم»، فإن «كم» للسؤال عن معين،",
     "en": "Among what al-Raḍī established is that kammiyya (quantity) is a relative word (nisba), that is, the attribute related to “kam” (how many), namely the specific number given in answer to “kam”; for “kam” asks about something specific."},
    {"type": "pair",
     "ar": "فخرج المجموع عن تعريف العدد حتى الألوف والمآت، ودخل رجل ورجلان على تقدير دخول واحد واثنين،",
     "en": "So the plurals are excluded from the definition of number, even “thousands” and “hundreds”, while rajul (a man) and rajulān (two men) are included on the supposition that “one” and “two” are included."},
    {"type": "pair",
     "ar": "فأخرج رجلا ورجلين بإرادة ما وضع لكمية الشيء فحسب، ورجل ورجلان وضعا للماهية وكميتها، كما ذكره الشارح هذا،",
     "en": "So he excluded rajul and rajulayn by meaning “what is imposed for the quantity of a thing only”, whereas rajul and rajulān are imposed for the quiddity and its quantity—as the Commentator mentioned. This [is so];"},
    {"type": "pair",
     "ar": "وفي كون «كم» سؤالا عن العدد المعين بحث كيف، ولا ينكر صحة الجواب عن \"كم رجلا عندك\" بقولك: ألوف ومآت",
     "en": "but there is room for discussion in “kam” being a question about a specific number—how [could it be], when the validity of answering “kam rajulan ʿindaka?” (how many men do you have?) with “thousands and hundreds” is not denied?"},
    {"type": "pair",
     "ar": "إلا أن يقال: هذا ليس جوابا عن السؤال بكم، بل اعترافا بعدم العلم بما سئل عنه، وبيان ما سئل عنه بقدر الاستطاعة،",
     "en": "Unless it be said: this is not an answer to the question with kam, but an admission of not knowing what was asked about, and a statement of what was asked about as far as one is able."},
    {"type": "pair",
     "ar": "ولا يشكل بالتنوين؛ لأن ما عبارة عن الاسم، فلا يتوهمن أن كم ليس مخصوصا بالسؤال عن العدد،",
     "en": "Nor is there a difficulty from tanwīn, because “mā” refers to the noun; so let it not be imagined that kam is not restricted to asking about number;"},
    # REVIEW: «وإلا لم يكن المسامحة كما لأن ذلك من التباس الكم الحكمي بكم اللغوي» is printed so (with «كما», printed with shadda and tanwin); the sense is unclear. Transcribed as printed; translation tentative.
    {"type": "pair",
     "ar": "وإلا لم يكن المسامحة كما لأن ذلك من التباس الكم الحكمي بكم اللغوي.",
     "en": "otherwise the loose usage would not be [a case of] kamm (quantity), because that comes from confusing philosophical quantity (al-kamm al-ḥikamī) with the linguistic kam."},
]
