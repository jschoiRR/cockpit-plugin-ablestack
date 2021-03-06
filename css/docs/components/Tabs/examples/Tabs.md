---
id: Tabs
section: components
cssPrefix: pf-c-tabs
---import './Tabs.css'

## Examples

### Default

```html
<div class="pf-c-tabs" id="default-example">
  <button class="pf-c-tabs__scroll-button" disabled aria-hidden="true" aria-label="Scroll left">
    <i class="fas fa-angle-left" aria-hidden="true"></i>
  </button>
  <ul class="pf-c-tabs__list">
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="default-example-users-link">
        <span class="pf-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-c-tabs__item pf-m-current">
      <button class="pf-c-tabs__link" id="default-example-containers-link">
        <span class="pf-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="default-example-database-link">
        <span class="pf-c-tabs__item-text">Database</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="default-example-server-link">
        <span class="pf-c-tabs__item-text">Server</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="default-example-system-link">
        <span class="pf-c-tabs__item-text">System</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="default-example-network-wired-link">
        <span class="pf-c-tabs__item-text">Network</span>
      </button>
    </li>
  </ul>
  <button class="pf-c-tabs__scroll-button" disabled aria-hidden="true" aria-label="Scroll right">
    <i class="fas fa-angle-right" aria-hidden="true"></i>
  </button>
</div>
```

### Default overflow beginning of list

```html
<div class="pf-c-tabs pf-m-scrollable" id="default-overflow-beginning-of-list-example">
  <button class="pf-c-tabs__scroll-button" disabled aria-label="Scroll left">
    <i class="fas fa-angle-left" aria-hidden="true"></i>
  </button>
  <ul class="pf-c-tabs__list">
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="default-overflow-beginning-of-list-example-users-link">
        <span class="pf-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-c-tabs__item pf-m-current">
      <button class="pf-c-tabs__link" id="default-overflow-beginning-of-list-example-containers-link">
        <span class="pf-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="default-overflow-beginning-of-list-example-database-link">
        <span class="pf-c-tabs__item-text">Database</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="default-overflow-beginning-of-list-example-server-link">
        <span class="pf-c-tabs__item-text">Server</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="default-overflow-beginning-of-list-example-system-link">
        <span class="pf-c-tabs__item-text">System</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="default-overflow-beginning-of-list-example-network-wired-link">
        <span class="pf-c-tabs__item-text">Network</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="default-overflow-beginning-of-list-example-cloud-link">
        <span class="pf-c-tabs__item-text">Hybrid Cloud</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="default-overflow-beginning-of-list-example-automation-link">
        <span class="pf-c-tabs__item-text">Automation</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="default-overflow-beginning-of-list-example-files-link">
        <span class="pf-c-tabs__item-text">Files</span>
      </button>
    </li>
  </ul>
  <button class="pf-c-tabs__scroll-button" aria-label="Scroll right">
    <i class="fas fa-angle-right" aria-hidden="true"></i>
  </button>
</div>
```

### Accessibility

| Attribute            | Applied to                  | Outcome                                                                                                          |
| -------------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `disabled`           | `.pf-c-tabs__scroll-button` | Indicates that a scroll button is disabled, when at the first or last item of a list. **Required when disabled** |
| `aria-hidden="true"` | `.pf-c-tabs__scroll-button` | Hides the icon from assistive technologies.**Required when not scrollable**                                      |

### Usage

| Class                       | Applied to   | Outcome                                   |
| --------------------------- | ------------ | ----------------------------------------- |
| `.pf-m-scrollable`          | `.pf-c-tabs` | Enables the directional scroll buttons.   |
| `.pf-c-tabs__scroll-button` | `<button>`   | Initiates a tabs component scroll button. |

### Vertical

```html
<div class="pf-c-tabs pf-m-vertical" id="vertical-example">
  <ul class="pf-c-tabs__list">
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="vertical-example-users-link">
        <span class="pf-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-c-tabs__item pf-m-current">
      <button class="pf-c-tabs__link" id="vertical-example-containers-link">
        <span class="pf-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="vertical-example-database-link">
        <span class="pf-c-tabs__item-text">Database</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="vertical-example-server-link">
        <span class="pf-c-tabs__item-text">Server</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="vertical-example-system-link">
        <span class="pf-c-tabs__item-text">System</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="vertical-example-network-wired-link">
        <span class="pf-c-tabs__item-text">Network</span>
      </button>
    </li>
  </ul>
</div>
```

### Box

```html
<div class="pf-c-tabs pf-m-box" id="box-example">
  <button class="pf-c-tabs__scroll-button" disabled aria-hidden="true" aria-label="Scroll left">
    <i class="fas fa-angle-left" aria-hidden="true"></i>
  </button>
  <ul class="pf-c-tabs__list">
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="box-example-users-link">
        <span class="pf-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-c-tabs__item pf-m-current">
      <button class="pf-c-tabs__link" id="box-example-containers-link">
        <span class="pf-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="box-example-database-link">
        <span class="pf-c-tabs__item-text">Database</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="box-example-server-link">
        <span class="pf-c-tabs__item-text">Server</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="box-example-system-link">
        <span class="pf-c-tabs__item-text">System</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="box-example-network-wired-link">
        <span class="pf-c-tabs__item-text">Network</span>
      </button>
    </li>
  </ul>
  <button class="pf-c-tabs__scroll-button" disabled aria-hidden="true" aria-label="Scroll right">
    <i class="fas fa-angle-right" aria-hidden="true"></i>
  </button>
</div>
```

### Box overflow

```html
<div class="pf-c-tabs pf-m-box pf-m-scrollable" id="box-overflow-example">
  <button class="pf-c-tabs__scroll-button" disabled aria-label="Scroll left">
    <i class="fas fa-angle-left" aria-hidden="true"></i>
  </button>
  <ul class="pf-c-tabs__list">
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="box-overflow-example-users-link">
        <span class="pf-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-c-tabs__item pf-m-current">
      <button class="pf-c-tabs__link" id="box-overflow-example-containers-link">
        <span class="pf-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="box-overflow-example-database-link">
        <span class="pf-c-tabs__item-text">Database</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="box-overflow-example-server-link">
        <span class="pf-c-tabs__item-text">Server</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="box-overflow-example-system-link">
        <span class="pf-c-tabs__item-text">System</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="box-overflow-example-network-wired-link">
        <span class="pf-c-tabs__item-text">Network</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="box-overflow-example-cloud-link">
        <span class="pf-c-tabs__item-text">Hybrid Cloud</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="box-overflow-example-automation-link">
        <span class="pf-c-tabs__item-text">Automation</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="box-overflow-example-files-link">
        <span class="pf-c-tabs__item-text">Files</span>
      </button>
    </li>
  </ul>
  <button class="pf-c-tabs__scroll-button" aria-label="Scroll right">
    <i class="fas fa-angle-right" aria-hidden="true"></i>
  </button>
</div>
```

### Box vertical

```html
<div class="pf-c-tabs pf-m-box pf-m-vertical" id="box-vertical-example">
  <ul class="pf-c-tabs__list">
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="box-vertical-example-users-link">
        <span class="pf-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-c-tabs__item pf-m-current">
      <button class="pf-c-tabs__link" id="box-vertical-example-containers-link">
        <span class="pf-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="box-vertical-example-database-link">
        <span class="pf-c-tabs__item-text">Database</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="box-vertical-example-server-link">
        <span class="pf-c-tabs__item-text">Server</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="box-vertical-example-system-link">
        <span class="pf-c-tabs__item-text">System</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="box-vertical-example-network-wired-link">
        <span class="pf-c-tabs__item-text">Network</span>
      </button>
    </li>
  </ul>
</div>
```

### Box tabs color scheme light 300

```html
<div class="pf-c-tabs pf-m-box pf-m-color-scheme--light-300" id="Box-tabs-alt-color-scheme">
  <button class="pf-c-tabs__scroll-button" disabled aria-hidden="true" aria-label="Scroll left">
    <i class="fas fa-angle-left" aria-hidden="true"></i>
  </button>
  <ul class="pf-c-tabs__list">
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="Box-tabs-alt-color-scheme-users-link">
        <span class="pf-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-c-tabs__item pf-m-current">
      <button class="pf-c-tabs__link" id="Box-tabs-alt-color-scheme-containers-link">
        <span class="pf-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="Box-tabs-alt-color-scheme-database-link">
        <span class="pf-c-tabs__item-text">Database</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="Box-tabs-alt-color-scheme-server-link">
        <span class="pf-c-tabs__item-text">Server</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="Box-tabs-alt-color-scheme-system-link">
        <span class="pf-c-tabs__item-text">System</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="Box-tabs-alt-color-scheme-network-wired-link">
        <span class="pf-c-tabs__item-text">Network</span>
      </button>
    </li>
  </ul>
  <button class="pf-c-tabs__scroll-button" disabled aria-hidden="true" aria-label="Scroll right">
    <i class="fas fa-angle-right" aria-hidden="true"></i>
  </button>
</div>
<div className="tabs-example-block tabs-example-block--m-color-scheme--light-300"></div>
```

### Inset

```html
<div class="pf-c-tabs pf-m-inset-sm-on-md pf-m-inset-lg-on-lg pf-m-inset-2xl-on-xl" id="inset-example">
  <button class="pf-c-tabs__scroll-button" disabled aria-hidden="true" aria-label="Scroll left">
    <i class="fas fa-angle-left" aria-hidden="true"></i>
  </button>
  <ul class="pf-c-tabs__list">
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="inset-example-users-link">
        <span class="pf-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-c-tabs__item pf-m-current">
      <button class="pf-c-tabs__link" id="inset-example-containers-link">
        <span class="pf-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="inset-example-database-link">
        <span class="pf-c-tabs__item-text">Database</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="inset-example-server-link">
        <span class="pf-c-tabs__item-text">Server</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="inset-example-system-link">
        <span class="pf-c-tabs__item-text">System</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="inset-example-network-wired-link">
        <span class="pf-c-tabs__item-text">Network</span>
      </button>
    </li>
  </ul>
  <button class="pf-c-tabs__scroll-button" disabled aria-hidden="true" aria-label="Scroll right">
    <i class="fas fa-angle-right" aria-hidden="true"></i>
  </button>
</div>
```

### Inset box

```html
<div class="pf-c-tabs pf-m-box pf-m-inset-sm-on-md pf-m-inset-lg-on-lg pf-m-inset-2xl-on-xl" id="inset-box-example">
  <button class="pf-c-tabs__scroll-button" disabled aria-hidden="true" aria-label="Scroll left">
    <i class="fas fa-angle-left" aria-hidden="true"></i>
  </button>
  <ul class="pf-c-tabs__list">
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="inset-box-example-users-link">
        <span class="pf-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-c-tabs__item pf-m-current">
      <button class="pf-c-tabs__link" id="inset-box-example-containers-link">
        <span class="pf-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="inset-box-example-database-link">
        <span class="pf-c-tabs__item-text">Database</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="inset-box-example-server-link">
        <span class="pf-c-tabs__item-text">Server</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="inset-box-example-system-link">
        <span class="pf-c-tabs__item-text">System</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="inset-box-example-network-wired-link">
        <span class="pf-c-tabs__item-text">Network</span>
      </button>
    </li>
  </ul>
  <button class="pf-c-tabs__scroll-button" disabled aria-hidden="true" aria-label="Scroll right">
    <i class="fas fa-angle-right" aria-hidden="true"></i>
  </button>
</div>
```

### Usage

| Class                                                                     | Applied to   | Outcome                                                                                           |
| ------------------------------------------------------------------------- | ------------ | ------------------------------------------------------------------------------------------------- |
| `.pf-m-inset-{none, sm, md, lg, xl, 2xl, 3xl}{-on-[sm, md, lg, xl, 2xl]}` | `.pf-c-tabs` | Modifies the tabs component padding/inset to visually match padding of other adjacent components. |

### Icons and text

```html
<div class="pf-c-tabs" id="icons-example">
  <button class="pf-c-tabs__scroll-button" disabled aria-hidden="true" aria-label="Scroll left">
    <i class="fas fa-angle-left" aria-hidden="true"></i>
  </button>
  <ul class="pf-c-tabs__list">
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="icons-example-users-link">
        <span class="pf-c-tabs__item-icon" aria-hidden="true">
          <i class="fas fa-fas fa-users"></i>
        </span>
        <span class="pf-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-c-tabs__item pf-m-current">
      <button class="pf-c-tabs__link" id="icons-example-containers-link">
        <span class="pf-c-tabs__item-icon" aria-hidden="true">
          <i class="fas fa-fas fa-box"></i>
        </span>
        <span class="pf-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="icons-example-database-link">
        <span class="pf-c-tabs__item-icon" aria-hidden="true">
          <i class="fas fa-database"></i>
        </span>
        <span class="pf-c-tabs__item-text">Database</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="icons-example-server-link">
        <span class="pf-c-tabs__item-icon" aria-hidden="true">
          <i class="fas fa-server"></i>
        </span>
        <span class="pf-c-tabs__item-text">Server</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="icons-example-system-link">
        <span class="pf-c-tabs__item-icon" aria-hidden="true">
          <i class="fas fa-laptop"></i>
        </span>
        <span class="pf-c-tabs__item-text">System</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="icons-example-network-wired-link">
        <span class="pf-c-tabs__item-icon" aria-hidden="true">
          <i class="fas fa-project-diagram"></i>
        </span>
        <span class="pf-c-tabs__item-text">Network</span>
      </button>
    </li>
  </ul>
  <button class="pf-c-tabs__scroll-button" disabled aria-hidden="true" aria-label="Scroll right">
    <i class="fas fa-angle-right" aria-hidden="true"></i>
  </button>
</div>
```

### Tabs with sub tabs

```html
<div class="pf-c-tabs pf-m-scrollable" id="default-parent-example">
  <button class="pf-c-tabs__scroll-button" aria-label="Scroll left">
    <i class="fas fa-angle-left" aria-hidden="true"></i>
  </button>
  <ul class="pf-c-tabs__list">
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="default-parent-example-users-link">
        <span class="pf-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-c-tabs__item pf-m-current">
      <button class="pf-c-tabs__link" id="default-parent-example-containers-link">
        <span class="pf-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="default-parent-example-database-link">
        <span class="pf-c-tabs__item-text">Database</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="default-parent-example-server-link">
        <span class="pf-c-tabs__item-text">Server</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="default-parent-example-system-link">
        <span class="pf-c-tabs__item-text">System</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="default-parent-example-network-wired-link">
        <span class="pf-c-tabs__item-text">Network</span>
      </button>
    </li>
  </ul>
  <button class="pf-c-tabs__scroll-button" aria-label="Scroll right">
    <i class="fas fa-angle-right" aria-hidden="true"></i>
  </button>
</div>
<div class="pf-c-tabs pf-m-secondary pf-m-scrollable" id="default-child-example">
  <button class="pf-c-tabs__scroll-button" aria-label="Scroll left">
    <i class="fas fa-angle-left" aria-hidden="true"></i>
  </button>
  <ul class="pf-c-tabs__list">
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="default-child-example-sub-1-link">
        <span class="pf-c-tabs__item-text">Item 1</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="default-child-example-sub-2-link">
        <span class="pf-c-tabs__item-text">Item 2</span>
      </button>
    </li>
    <li class="pf-c-tabs__item pf-m-current">
      <button class="pf-c-tabs__link" id="default-child-example-sub-3-link">
        <span class="pf-c-tabs__item-text">Item 3</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="default-child-example-sub-4-link">
        <span class="pf-c-tabs__item-text">Item 4</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="default-child-example-sub-5-link">
        <span class="pf-c-tabs__item-text">Item 5</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="default-child-example-sub-6-link">
        <span class="pf-c-tabs__item-text">Item 6</span>
      </button>
    </li>
  </ul>
  <button class="pf-c-tabs__scroll-button" aria-label="Scroll right">
    <i class="fas fa-angle-right" aria-hidden="true"></i>
  </button>
</div>
```

### Box tabs with sub tabs

```html
<div class="pf-c-tabs pf-m-box pf-m-scrollable" id="box-parent-example">
  <button class="pf-c-tabs__scroll-button" aria-label="Scroll left">
    <i class="fas fa-angle-left" aria-hidden="true"></i>
  </button>
  <ul class="pf-c-tabs__list">
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="box-parent-example-users-link">
        <span class="pf-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-c-tabs__item pf-m-current">
      <button class="pf-c-tabs__link" id="box-parent-example-containers-link">
        <span class="pf-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="box-parent-example-database-link">
        <span class="pf-c-tabs__item-text">Database</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="box-parent-example-server-link">
        <span class="pf-c-tabs__item-text">Server</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="box-parent-example-system-link">
        <span class="pf-c-tabs__item-text">System</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="box-parent-example-network-wired-link">
        <span class="pf-c-tabs__item-text">Network</span>
      </button>
    </li>
  </ul>
  <button class="pf-c-tabs__scroll-button" aria-label="Scroll right">
    <i class="fas fa-angle-right" aria-hidden="true"></i>
  </button>
</div>
<div class="pf-c-tabs pf-m-secondary pf-m-scrollable" id="box-child-example">
  <button class="pf-c-tabs__scroll-button" aria-label="Scroll left">
    <i class="fas fa-angle-left" aria-hidden="true"></i>
  </button>
  <ul class="pf-c-tabs__list">
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="box-child-example-sub-1-link">
        <span class="pf-c-tabs__item-text">Item 1</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="box-child-example-sub-2-link">
        <span class="pf-c-tabs__item-text">Item 2</span>
      </button>
    </li>
    <li class="pf-c-tabs__item pf-m-current">
      <button class="pf-c-tabs__link" id="box-child-example-sub-3-link">
        <span class="pf-c-tabs__item-text">Item 3</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="box-child-example-sub-4-link">
        <span class="pf-c-tabs__item-text">Item 4</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="box-child-example-sub-5-link">
        <span class="pf-c-tabs__item-text">Item 5</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="box-child-example-sub-6-link">
        <span class="pf-c-tabs__item-text">Item 6</span>
      </button>
    </li>
  </ul>
  <button class="pf-c-tabs__scroll-button" aria-label="Scroll right">
    <i class="fas fa-angle-right" aria-hidden="true"></i>
  </button>
</div>
```

### Filled

```html
<div class="pf-c-tabs pf-m-fill" id="filled-example">
  <button class="pf-c-tabs__scroll-button" disabled aria-hidden="true" aria-label="Scroll left">
    <i class="fas fa-angle-left" aria-hidden="true"></i>
  </button>
  <ul class="pf-c-tabs__list">
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="filled-example-users-link">
        <span class="pf-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-c-tabs__item pf-m-current">
      <button class="pf-c-tabs__link" id="filled-example-containers-link">
        <span class="pf-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="filled-example-database-link">
        <span class="pf-c-tabs__item-text">Database</span>
      </button>
    </li>
  </ul>
  <button class="pf-c-tabs__scroll-button" disabled aria-hidden="true" aria-label="Scroll right">
    <i class="fas fa-angle-right" aria-hidden="true"></i>
  </button>
</div>
```

### Filled with icons

```html
<div class="pf-c-tabs pf-m-fill" id="filled-with-icons-example">
  <button class="pf-c-tabs__scroll-button" disabled aria-hidden="true" aria-label="Scroll left">
    <i class="fas fa-angle-left" aria-hidden="true"></i>
  </button>
  <ul class="pf-c-tabs__list">
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="filled-with-icons-example-users-link">
        <span class="pf-c-tabs__item-icon" aria-hidden="true">
          <i class="fas fa-fas fa-users"></i>
        </span>
        <span class="pf-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-c-tabs__item pf-m-current">
      <button class="pf-c-tabs__link" id="filled-with-icons-example-containers-link">
        <span class="pf-c-tabs__item-icon" aria-hidden="true">
          <i class="fas fa-fas fa-box"></i>
        </span>
        <span class="pf-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="filled-with-icons-example-database-link">
        <span class="pf-c-tabs__item-icon" aria-hidden="true">
          <i class="fas fa-database"></i>
        </span>
        <span class="pf-c-tabs__item-text">Database</span>
      </button>
    </li>
  </ul>
  <button class="pf-c-tabs__scroll-button" disabled aria-hidden="true" aria-label="Scroll right">
    <i class="fas fa-angle-right" aria-hidden="true"></i>
  </button>
</div>
```

### Filled box

```html
<div class="pf-c-tabs pf-m-fill pf-m-box" id="filled-box-example">
  <button class="pf-c-tabs__scroll-button" disabled aria-hidden="true" aria-label="Scroll left">
    <i class="fas fa-angle-left" aria-hidden="true"></i>
  </button>
  <ul class="pf-c-tabs__list">
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="filled-box-example-users-link">
        <span class="pf-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-c-tabs__item pf-m-current">
      <button class="pf-c-tabs__link" id="filled-box-example-containers-link">
        <span class="pf-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="filled-box-example-database-link">
        <span class="pf-c-tabs__item-text">Database</span>
      </button>
    </li>
  </ul>
  <button class="pf-c-tabs__scroll-button" disabled aria-hidden="true" aria-label="Scroll right">
    <i class="fas fa-angle-right" aria-hidden="true"></i>
  </button>
</div>
```

### Filled box with icons

```html
<div class="pf-c-tabs pf-m-fill pf-m-box" id="filled-box-with-icons-example">
  <button class="pf-c-tabs__scroll-button" disabled aria-hidden="true" aria-label="Scroll left">
    <i class="fas fa-angle-left" aria-hidden="true"></i>
  </button>
  <ul class="pf-c-tabs__list">
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="filled-box-with-icons-example-users-link">
        <span class="pf-c-tabs__item-icon" aria-hidden="true">
          <i class="fas fa-fas fa-users"></i>
        </span>
        <span class="pf-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-c-tabs__item pf-m-current">
      <button class="pf-c-tabs__link" id="filled-box-with-icons-example-containers-link">
        <span class="pf-c-tabs__item-icon" aria-hidden="true">
          <i class="fas fa-fas fa-box"></i>
        </span>
        <span class="pf-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-c-tabs__item">
      <button class="pf-c-tabs__link" id="filled-box-with-icons-example-database-link">
        <span class="pf-c-tabs__item-icon" aria-hidden="true">
          <i class="fas fa-database"></i>
        </span>
        <span class="pf-c-tabs__item-text">Database</span>
      </button>
    </li>
  </ul>
  <button class="pf-c-tabs__scroll-button" disabled aria-hidden="true" aria-label="Scroll right">
    <i class="fas fa-angle-right" aria-hidden="true"></i>
  </button>
</div>
```

## Usage

| Class        | Applied to   | Outcome                                                     |
| ------------ | ------------ | ----------------------------------------------------------- |
| `.pf-m-fill` | `.pf-c-tabs` | Modifies the tabs to fill the available space. **Required** |

### Using the nav element

```html
<nav class="pf-c-tabs pf-m-scrollable" aria-label="Local" id="default-scroll-nav-example">
  <button class="pf-c-tabs__scroll-button" aria-label="Scroll left">
    <i class="fas fa-angle-left" aria-hidden="true"></i>
  </button>
  <ul class="pf-c-tabs__list">
    <li class="pf-c-tabs__item">
      <a class="pf-c-tabs__link" href="#" id="default-scroll-nav-example-users-link">
        <span class="pf-c-tabs__item-text">Users</span>
      </a>
    </li>
    <li class="pf-c-tabs__item pf-m-current">
      <a class="pf-c-tabs__link" href="#" id="default-scroll-nav-example-containers-link">
        <span class="pf-c-tabs__item-text">Containers</span>
      </a>
    </li>
    <li class="pf-c-tabs__item">
      <a class="pf-c-tabs__link" href="#" id="default-scroll-nav-example-database-link">
        <span class="pf-c-tabs__item-text">Database</span>
      </a>
    </li>
    <li class="pf-c-tabs__item">
      <a class="pf-c-tabs__link" href="#" id="default-scroll-nav-example-server-link">
        <span class="pf-c-tabs__item-text">Server</span>
      </a>
    </li>
    <li class="pf-c-tabs__item">
      <a class="pf-c-tabs__link" href="#" id="default-scroll-nav-example-system-link">
        <span class="pf-c-tabs__item-text">System</span>
      </a>
    </li>
    <li class="pf-c-tabs__item">
      <a class="pf-c-tabs__link" href="#" id="default-scroll-nav-example-network-wired-link">
        <span class="pf-c-tabs__item-text">Network</span>
      </a>
    </li>
  </ul>
  <button class="pf-c-tabs__scroll-button" aria-label="Scroll right">
    <i class="fas fa-angle-right" aria-hidden="true"></i>
  </button>
</nav>
```

### Sub nav using the nav element

```html
<nav class="pf-c-tabs" aria-label="Local" id="primary-nav-example">
  <button class="pf-c-tabs__scroll-button" disabled aria-hidden="true" aria-label="Scroll left">
    <i class="fas fa-angle-left" aria-hidden="true"></i>
  </button>
  <ul class="pf-c-tabs__list">
    <li class="pf-c-tabs__item">
      <a class="pf-c-tabs__link" href="#" id="primary-nav-example-users-link">
        <span class="pf-c-tabs__item-text">Users</span>
      </a>
    </li>
    <li class="pf-c-tabs__item pf-m-current">
      <a class="pf-c-tabs__link" href="#" id="primary-nav-example-containers-link">
        <span class="pf-c-tabs__item-text">Containers</span>
      </a>
    </li>
    <li class="pf-c-tabs__item">
      <a class="pf-c-tabs__link" href="#" id="primary-nav-example-database-link">
        <span class="pf-c-tabs__item-text">Database</span>
      </a>
    </li>
    <li class="pf-c-tabs__item">
      <a class="pf-c-tabs__link" href="#" id="primary-nav-example-server-link">
        <span class="pf-c-tabs__item-text">Server</span>
      </a>
    </li>
    <li class="pf-c-tabs__item">
      <a class="pf-c-tabs__link" href="#" id="primary-nav-example-system-link">
        <span class="pf-c-tabs__item-text">System</span>
      </a>
    </li>
    <li class="pf-c-tabs__item">
      <a class="pf-c-tabs__link" href="#" id="primary-nav-example-network-wired-link">
        <span class="pf-c-tabs__item-text">Network</span>
      </a>
    </li>
  </ul>
  <button class="pf-c-tabs__scroll-button" disabled aria-hidden="true" aria-label="Scroll right">
    <i class="fas fa-angle-right" aria-hidden="true"></i>
  </button>
</nav>
<nav class="pf-c-tabs pf-m-secondary" aria-label="Local secondary" id="secondary-nav-example">
  <button class="pf-c-tabs__scroll-button" disabled aria-hidden="true" aria-label="Scroll left">
    <i class="fas fa-angle-left" aria-hidden="true"></i>
  </button>
  <ul class="pf-c-tabs__list">
    <li class="pf-c-tabs__item">
      <a class="pf-c-tabs__link" href="#" id="secondary-nav-example-sub-1-link">
        <span class="pf-c-tabs__item-text">Item 1</span>
      </a>
    </li>
    <li class="pf-c-tabs__item">
      <a class="pf-c-tabs__link" href="#" id="secondary-nav-example-sub-2-link">
        <span class="pf-c-tabs__item-text">Item 2</span>
      </a>
    </li>
    <li class="pf-c-tabs__item pf-m-current">
      <a class="pf-c-tabs__link" href="#" id="secondary-nav-example-sub-3-link">
        <span class="pf-c-tabs__item-text">Item 3</span>
      </a>
    </li>
    <li class="pf-c-tabs__item">
      <a class="pf-c-tabs__link" href="#" id="secondary-nav-example-sub-4-link">
        <span class="pf-c-tabs__item-text">Item 4</span>
      </a>
    </li>
    <li class="pf-c-tabs__item">
      <a class="pf-c-tabs__link" href="#" id="secondary-nav-example-sub-5-link">
        <span class="pf-c-tabs__item-text">Item 5</span>
      </a>
    </li>
    <li class="pf-c-tabs__item">
      <a class="pf-c-tabs__link" href="#" id="secondary-nav-example-sub-6-link">
        <span class="pf-c-tabs__item-text">Item 6</span>
      </a>
    </li>
  </ul>
  <button class="pf-c-tabs__scroll-button" disabled aria-hidden="true" aria-label="Scroll right">
    <i class="fas fa-angle-right" aria-hidden="true"></i>
  </button>
</nav>
```

The tabs component should only be used to change content views within a page. The similar-looking but semantically different [horizontal nav component](/documentation/core/components/nav) is available for general navigation use cases.

Tabs should be used with the [tab content component](/documentation/core/components/tabcontent).

Whenever a list of tabs is unique on the current page, it can be used in a `<nav>` element. Cases where the same set of tabs are duplicated in multiple regions on a page (e.g. cards on a dashboard) are less likely to benefit from using the `<nav>` element.

### Accessibility

| Attribute                       | Applied to                                      | Outcome                                                                                                                                  |
| ------------------------------- | ----------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `aria-label="Descriptive text"` | `nav.pf-c-tabs`, `nav.pf-c-tabs.pf-m-secondary` | Gives the `<nav>` an accessible label. **Required when `.pf-c-tabs` is used with `<nav>`**                                               |
| `aria-label="Descriptive text"` | `.pf-c-inline-edit__toggle > button`            | Provides an accessible description for toggle button. **Required**                                                                       |
| `disabled`                      | `.pf-c-tabs__scroll-button`                     | Indicates that a scroll button is disable, typically when at the first or last item of a list or scroll buttons are hidden. **Required** |

### Usage

| Class                                                            | Applied to         | Outcome                                                                                           |
| ---------------------------------------------------------------- | ------------------ | ------------------------------------------------------------------------------------------------- |
| `.pf-c-tabs`                                                     | `<nav>`, `<div>`   | Initiates the tabs component. **Required**                                                        |
| `.pf-c-tabs__list`                                               | `<ul>`             | Initiates a tabs component list. **Required**                                                     |
| `.pf-c-tabs__item`                                               | `<li>`             | Initiates a tabs component item. **Required**                                                     |
| `.pf-c-tabs__item-text`                                          | `<span>`           | Initiates a tabs component item icon. **Required**                                                |
| `.pf-c-tabs__item-icon`                                          | `<span>`           | Initiates a tabs component item text. **Required**                                                |
| `.pf-c-tabs__link`                                               | `<button>`, `<a>`  | Initiates a tabs component link. **Required**                                                     |
| `.pf-c-tabs__scroll-button`                                      | `<button>`         | Initiates a tabs component scroll button.                                                         |
| `.pf-m-secondary`                                                | `.pf-c-tabs`       | Applies secondary styling to the tab component.                                                   |
| `.pf-m-no-border-bottom`                                         | `.pf-c-tabs`       | Removes bottom border from a tab component.                                                       |
| `.pf-m-box`                                                      | `.pf-c-tabs`       | Applies box styling to the tab component.                                                         |
| `.pf-m-vertical`                                                 | `.pf-c-tabs`       | Applies vertical styling to the tab component.                                                    |
| `.pf-m-fill`                                                     | `.pf-c-tabs`       | Modifies the tabs to fill the available space.                                                    |
| `.pf-m-current`                                                  | `.pf-c-tabs__item` | Indicates that a tab item is currently selected.                                                  |
| `.pf-m-inset-{none, sm, md, lg, xl, 2xl}{-on-[md, lg, xl, 2xl]}` | `.pf-c-tabs`       | Modifies the tabs component padding/inset to visually match padding of other adjacent components. |
| `.pf-m-color-scheme--light-300`                                  | `.pf-c-tabs`       | Modifies the tabs component tab background colors.                                                |
